from langchain_ollama import OllamaEmbeddings
from app.core.settings import settings
from app.ai.embeddings.base_embedding import BaseEmbedding


class OllamaEmbedding(BaseEmbedding):

    def __init__(self):

        self.embedding = OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL,
            base_url=settings.OLLAMA_BASE_URL
        )

    def embed_documents(self, documents):

        return self.embedding.embed_documents(
            [doc.page_content for doc in documents]
        )

    def embed_query(self, query: str):

        return self.embedding.embed_query(query)