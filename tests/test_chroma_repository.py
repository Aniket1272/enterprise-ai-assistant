from app.loaders.pdf_loader import PDFLoader
from app.processors.text_processor import TextProcessor
from app.chunking.chunk_service import ChunkService
from app.ai.embeddings.factory import EmbeddingFactory
from app.repositories.chroma_repository import ChromaRepository


def main():

    text = PDFLoader.load("uploads/sample.pdf")

    cleaned = TextProcessor().process(text)

    chunks = ChunkService.split(cleaned)

    embedding_service = EmbeddingFactory.create()

    embeddings = embedding_service.embed_documents(chunks)

    repository = ChromaRepository()

    ids = repository.save_documents(chunks, embeddings)

    print(f"Stored {len(ids)} vectors.")


if __name__ == "__main__":
    main()    