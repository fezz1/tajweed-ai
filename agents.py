import os
import json
from google import genai
from google.genai import types
from tavily import TavilyClient
from tools import rag_instance

ai_client = genai.Client()

def call_tavily_search(query: str) -> str:
    """Executes live open-web search parameter sweeps via Tavily API client."""
    try:
        tavily = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
        response = tavily.search(query=query, max_results=3)
        results = [f"Title: {r['title']}\nContent: {r['content']}" for r in response.get('results', [])]
        return "\n\n".join(results)
    except Exception as e:
        return f"Tavily search execution failed: {str(e)}"

def researcher_agent(state: dict) -> dict:
    """Agent 1: Researcher - Decides between RAG and Web Search based on intent."""
    query = state["current_query"]
    
    # Intent classification logic via Gemini routing prompt
    routing_prompt = (
        f"Analyze user query: '{query}'. If it requires timeless standard Quranic rules (like Izhar, Idgham, text details), "
        "reply with 'RAG'. If it asks about video links, software tools, external URLs, or modern apps, reply with 'WEB'."
    )
    
    decision = ai_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=routing_prompt
    ).text.strip().upper()
    
    state["routing_decision"] = decision
    
    if "RAG" in decision:
        context = rag_instance.vector_search(query)
        source_label = "Local FAISS Database (text-embedding-005)"
    else:
        context = call_tavily_search(query)
        source_label = "Live Tavily Web Search Engine"
        
    research_prompt = (
        f"Synthesize an educational explanation for query: '{query}'. "
        f"Using exclusively this extracted context information:\n{context}"
    )
    
    draft = ai_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=research_prompt
    ).text
    
    state["research_draft"] = draft
    state["metadata_sources"].append(source_label)
    return state

def reviewer_qa_agent(state: dict) -> dict:
    """Agent 2: Reviewer/QA - Inspects output quality and creates a validation feedback loop."""
    draft = state["research_draft"]
    query = state["current_query"]
    
    qa_prompt = (
        f"You are a strict QA verification inspector. Review this draft response for user question: '{query}'.\n"
        f"Draft:\n{draft}\n\n"
        "Ensure the language is respectful, correct, clear, and addresses the query. "
        "If it is perfect, return the original text directly. If it can be improved, rewrite it perfectly."
    )
    
    final_output = ai_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=qa_prompt
    ).text
    
    state["final_response"] = final_output
    state["pipeline_history"].append("QA_Review_Complete")
    return state
