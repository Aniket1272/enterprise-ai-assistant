from app.ai.embeddings.ollama_embedding import OllamaEmbedding


class EmbeddingFactory:

    @staticmethod
    def create():

        return OllamaEmbedding()