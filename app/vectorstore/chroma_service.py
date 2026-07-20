import chromadb
from chromadb.config import Settings
from app.core.settings import settings


class ChromaService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION
        )


    def get_collection(self):
        return self.collection    