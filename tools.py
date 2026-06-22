import numpy as np
import faiss
from google import genai
from google.genai import types

# Initialize structural client engine
ai_client = genai.Client()

class RAGEngine:
    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.index = None
        self.chunks = []
        
    def chunk_text(self, text: str) -> list[str]:
        """Performs precise structural character-bound semantic chunking."""
        words = text.split()
        chunks = []
        for i in range(0, len(words), self.chunk_size - self.overlap):
            chunk = " ".join(words[i:i + self.chunk_size])
            chunks.append(chunk)
        return chunks

    def get_embeddings(self, texts: list[str]) -> np.ndarray:
        """Generates semantic high-density vectors using Vertex AI text-embedding-005."""
        embeddings = []
        for text in texts:
            response = ai_client.models.embed_content(
                model="text-embedding-005",
                contents=text
            )
            # Handle list array extraction depending on batch formats
            if isinstance(response.embeddings, list):
                embeddings.append(response.embeddings[0].values)
            else:
                embeddings.append(response.embedding.values)
        return np.array(embeddings).astype('float32')

    def build_index(self, raw_text: str):
        """Builds and populations localized high-performance FAISS index matrix."""
        self.chunks = self.chunk_text(raw_text)
        if not self.chunks:
            return
        embeddings = self.get_embeddings(self.chunks)
        dimension = embeddings.shape[1]
        
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def vector_search(self, query: str, top_k: int = 2) -> str:
        """Executes Vector distance similarity matrix scans across local data rows."""
        if self.index is None or not self.chunks:
            return "No local RAG database initialized."
            
        query_vector = self.get_embeddings([query])
        distances, indices = self.index.search(query_vector, top_k)
        
        retrieved_contexts = []
        for idx in indices[0]:
            if idx != -1 and idx < len(self.chunks):
                retrieved_contexts.append(self.chunks[idx])
                
        return "\n---\n".join(retrieved_contexts)

# Instantiated static database instance for execution mapping
rag_instance = RAGEngine()
# Seeding initial baseline data array targets
baseline_data = (
    "Izhar rules state that Noon Sakinah or Tanween is pronounced clearly when throat letters follow. "
    "Idgham rules mean merging letters when letters of Yarmaloon follow. "
    "Iqlab changes Noon sound to Meem when Baa follows. "
    "Ikhfa conceals the sound lightly."
)
rag_instance.build_index(baseline_data)
