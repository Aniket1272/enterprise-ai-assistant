import chromadb
from chromadb.config import Settings


class ChromaService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="data/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )


    def get_collection(self):
        return self.collection    