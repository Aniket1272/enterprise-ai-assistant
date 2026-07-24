from app.ai.embeddings.factory import EmbeddingFactory
from app.repositories.chroma_repository import ChromaRepository


class RetrieverService:

    def __init__(self):
        
        self.embedding = EmbeddingFactory.create()
        self.repository = ChromaRepository()


    def retrieve(
            self,
            question,
            top_k=4
    ):
        query_vector = self.embedding.embed_query(
            question
        )    

        return self.repository.search_similar_documents(
            query_vector,
            top_k
        )

    def retrieve_context(self, question, top_k=4):

        result = self.retrieve(question, top_k)

        return "\n\n".join(result["documents"][0])