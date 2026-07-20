import uuid

from app.vectorstore.chroma_service import ChromaService


class ChromaRepository:

    def __init__(self):
        
        self.collection = ChromaService.get_collection()

    def save_documents(self, chunks, embeddings):

        ids = [str(uuid.uuid4()) for _ in chunks]

        self.collection.add(
            ids=ids,
            documents=[chunk.page_content for chunk in chunks],
            embeddings=embeddings,
            metadata=[
                {
                    "source": chunk.metadata.get("source", ""),
                    "page": chunk.metadata.get("page", -1),
                    "chunk_index": index
                }
                for index, chunk in enumerate(chunks)
            ]
        )

        return ids
