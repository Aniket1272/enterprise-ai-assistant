from langchain_openai import OpenAIEmbeddings

from app.config import settings


class EmbeddingService:

    def __init__(self):
        
        self.embedding_model = OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=settings.OPENAI_API_KEY,
        )

    
    def embed_documents(self, documents):

        return self.embedding_model.embed_documents(
            [doc.page_content for doc in documents]
        )    
    
    def embed_query(self, query: str):

        return self.embedding_model.embed_query(query)