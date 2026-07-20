from abc import ABC, abstractmethod


class BaseEmbedding(ABC):

    @abstractmethod
    def embed_documents(self, documents):

        pass

    @abstractmethod
    def embed_query(self, query: str):

        pass