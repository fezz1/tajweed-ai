Interactive Tajweed AI Companion 

Production-Grade Serverless Architecture Using Google Gen AI SDK & RAG 
Visual Elements: Icons representing multi-agent networks, cloud infrastructure, and Quranic education.

Project overviews & Objectives 
The Mission: Create an accessible, web-based tool to teach foundational Tajweed rules (Izhar, Idgham, Iqlab, Ikhfa).
Core Goals:
Deliver instant, rule-based text explanations.
Build a responsive, intuitive chat interface for users.
Implement an automated production pipeline for seamless updates.

The Architectural Evolution
Legacy System: Monolithic Python application utilizing rigid text-case conditional statements.
The Problem: Limited rule variations, high maintenance overhead, and no capability for real-time edge-case resolution.
The Solution: Migration to an autonomous Multi-Agent system powered by the Google Gen AI SDK.

Multi-Agent Team Topography
Orchestrator Agent (The Brain): Handles state sharing, session long-term memory, and intent classification.
Researcher Agent (The Information Gatherer): Intelligently bridges local RAG repositories and external query spaces.
Reviewer / QA Agent (The Validator): Establishes a production validation feedback loop to check output quality and correctness.

System Topology & Task Delegation
This diagram displays how the Google ADK manages communication flow, state inheritance, and the quality assurance feedback loop.

Hybrid Knowledge Matrix (RAG & Web) 
Local RAG Pipeline: High-density parsing, semantic text chunking, and vector encoding via Vertex AI's text-embedding-005.
Local Storage: In-memory FAISS vector database for millisecond-level similarity scans.
Live Web Fallback: Real-time open-web data aggregation powered by the Tavily Search API.
  User Submits Message          │
                      └─────────────┬────────────┘
                                                          │
                                                         ▼
                      ┌──────────────────────────┐
                      │       ORCHESTRATOR AGENT           │
                    │        (Intent Classification)                  │
                      └─────────────┬────────────┘
                                                          │
                   ┌──────────────┴────────────────┐
                   │                                                                                │
         [Match: Timeless Rule]     |     [Match: Media/External]
                   │                                   │
                  ▼                                  ▼
     ┌──────────────────────────┐      ┌─────────┐
     │    LOCAL RAG PIPELINE ││    LIVE WEB FALLBACK   │
     ├──────────────────────────┤      ├─────────┤
     │ * Vertex AI Embeddings │      │ * Tavily Search API               │
     │ * text-embedding-005     │      │ * Live Content Scrubbing     │
      * FAISS Vector Index     │      │ * Real-Time Resource URLs __│
     └────────────-┬────────────┘      └─────┬
                   │                                                                            │
                   └─────────-───┬────────────────┘
                                                      │
                               [Merged Context Injection]
                                                    │
                                                   ▼
                             ┌────────────────-┐
                             │Context-Grounded Draft │
                             └─────────────────

Hybrid Retrieval Matrix Router
This flowchart shows how the Orchestrator analyzes the intent of a query to dynamically select between the local vector database and the live internet.

LangSmith (Preferred for LLM Applications)
For AI-specific observability:
LangSmith tracing integrated with agent workflows
End-to-end visibility into:
Prompt execution
Tool calls
Retrieval results
Agent decision paths
Token usage
Latency bottlenecks
Failure analysis
Evaluation datasets for regression testing
Prompt and chain version tracking
Application Layer
             |
Agent / Workflow Layer
             |
------------------------
|  LangSmith       |
| Prompt Traces  |
| Tool Traces       |
| Evaluations       |
------------------------
              |
Google Cloud Platform
              |
------------------------
| Cloud Logging     |
| Cloud Monitoring |
| Alerting                  |
------------------------

LangSmith (Preferred for LLM Applications)
For AI-specific observability:
LangSmith tracing integrated with agent workflows
End-to-end visibility into:
Prompt execution
Tool calls
Retrieval results
Agent decision paths
Token usage
Latency bottlenecks
Failure analysis
Evaluation datasets for regression testing
Prompt and chain version tracking

LangSmith (LLM / GenAI Observability)
Tajweed application runs on an Agentic framework or LangChain to evaluate transcripts, provide conversational feedback, or grade pronunciation using an LLM backend.[ User Input ] ────► [Text ] ────► [ LangChain Application ] 
                     |
                     |                  
                                                                 │
                                                                ▼ 
                                                        [ LangSmith SaaS ] 
                                                                           │                                                 
                                                                           |
                                                                          ▼
                               [ Feedback / Evaluation ] (Score rules matching) 
Real-Time Grounding via Tavily API API Optimization
Advanced search depth tailored specifically for LLM context injection. Search Grounding: Bypasses static model training cutoffs to fetch real-time educational assets. Smart Content Extraction: Filters raw HTML clutter down to clean, high-density text snippets. Data Output: Returns structured source titles, verified URLs, and target content payloads. 

User Interface Wireframe Layout 
Framework: Single Page Application layout optimized across desktop monitors and mobile viewports. 
Chat Module: Fluid message log separating user questions from agent-generated answers. 
State Streaming: Active typing animations explicitly showing which background agent is processing data. 
Metadata Panel: Right-hand dashboard sidebar exposing clickable URL sources and pipeline execution steps.
Frontend Dashboard Layout 
This layout wireframe maps out how the user interface separates conversational content from technical metadata.
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  🌙 INTERACTIVE TAJWEED COMPANION                                 [ 🟢 Server Status ] │
├────────────────────────────────────────────────────────┬───────────────────────────────┤
│                                                                                                                                               │ [ PANEL 2: AGENT MONITOR ]                           │
│   [ PANEL 1: CHAT INTERFACE AREA ]                                                                            │                                                                                │
│                                                                                                                                               │  Active Agent: [Reviewer/QA]                             │
│  🤖 Bot: Assalamu Alaikum! Ask me about Tajweed rules.                                           │  Routing Path: [LOCAL RAG]                             │
│                                                                                                                                               │  Latency:      [240ms]                                           │
│  👤 Student: What are the letters of Izhar?                                                                      │                                                                               │
│                                                                                                                                               │───────────────────────────────│
│  🤖 Bot: The throat letters of Izhar are:                                                                            │ [ PANEL 3: SOURCES USED ]                            │
│          ء , ه , ع , ح , غ , خ                                                                                                           │                                                                                │
│          Example: مِنْ حَكِيمٍ                                                                                                          │  📁 canonical_tajweed.pdf                                 │
│                                                                                                                                               │  🔗 Line 42: Throat Letters                                 │
│                                                                                                                                               │  🛡️ Checked by QA Agent                                  │
├────────────────────────────────────────────────────────┴───────────────────────────────┤
│  ✍️ Ask a Tajweed rule or query...                                      [ 🚀 Send ]                                                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘

Stateful System Communication Flow 
Intent Routing: Orchestrator dynamically flags inputs as LOCAL (timeless standard rules) or WEB (media links or modern applications).
Sequential Pipeline: Prompt → State Context Isolation → Research Synthesis → Reviewer Optimization → User.
State Management: Unified JSON memory buffers that pass session states securely across agent boundaries.

RAG Route Verification: Send a POST request with the message "What is the rule of Izhar?". The Supervisor/Researcher will read the query, route it to RAG, extract matching records from the FAISS database via text-embedding-005, and return the verified text context.
Web Fallback Verification: Send a query like "Show me a youtube video link explaining how to pronounce idgham letters". The system will automatically route the request to WEB, execute a Tavily API search sweep, and return fresh external references.
Observability Logs: Open the Google Cloud Logs Explorer to inspect runtime trace paths and monitor the routing decisions made by your agent network.

The GitHub & Google Cloud Run Pipeline Architecture
This flow chart illustrates exactly how local code moves from Visual Studio, through your GitHub repository, and gets compiled automatically via Cloud Build to host the live serverless containers 

Production Infrastructure & Security
Serverless commute: Hosted on Google Cloud Run inside lightweight Docker runtime environments. 
Secret Management: Zero plain-text API keys; managed via Google Cloud Secret Manager.
Observability: Real-time execution tracking and metrics using Google Cloud Logs Explorer. 

Live Cloud Run Infrastructure Dashboards
These metrics dashboards show what my live dashboard will look like inside the Google Cloud Console. Once my Interactive Tajweed chatbot is successfully running, Google automatically generates charts tracking incoming HTTP request volume, container response latency, and health logs.

Cloud Production Infrastructure
This pipeline architecture shows how code updates automatically push from your development environment to a secure environment on Google Cloud Run.
┌─────────────────┐                ┌─────────────────┐                   ┌─────────────────┐
 │ Visual Studio                      │─────►│ GitHub                                │──────►│ Google Cloud                     │
 │ (Local Code)                      │                 │ Repository                          │                   │ Build Pipeline                     │
 └─────────────────┘                └─────────────────┘                    └────────┬────────┘
                                                              │
                                                     [Triggers Container]
                                                              │
                                                              ▼
 ┌─────────────────┐       🔒 IAM Roles                           ┌─────────────────┐
 │ Secret Manager                 │─────────────-─────-──►│ Google Cloud                    │
 │ (Protected Keys)                │   (Secret Accessor Policy)              │ Run (Serverless)               │
 └─────────────────┘                                                        └────────┬────────┘
                                                                                                                                 │
                                                                                                                   [Serves Public Traffic]
                                                                                                                                │
                                                                                                                               ▼
                                                                                                         ┌─────────────────┐
                                                                                                         │ Secure Live Link                │
                                                                                                         │    (HTTPS URL)                  │
                                                                                                         └─────────────────┘


Project Summary & Technical Roadmap
Current Accomplishments: Live public serverless chatbot routing queries automatically with zero idle cloud costs. 


