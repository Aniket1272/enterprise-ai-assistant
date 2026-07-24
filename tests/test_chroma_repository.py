from app.loaders.pdf_loader import PDFLoader
from app.processors.text_processor import TextProcessor
from app.chunking.chunk_service import ChunkService
from app.ai.embeddings.factory import EmbeddingFactory
from app.repositories.chroma_repository import ChromaRepository


def main():

    text = PDFLoader.load("uploads/sample.pdf")

    print("=" * 60)
    print("RAW TEXT")
    print("=" * 60)
    print(text[:1000])


    processed = TextProcessor.process(text)

    print("=" * 60)
    print("PROCESSED TEXT")
    print("=" * 60)
    print(processed[:1000])


    chunks = ChunkService().split(processed)

    print("=" * 60)
    print("FIRST CHUNK")
    print("=" * 60)
    print(chunks[0].page_content)
    
    embedding_service = EmbeddingFactory.create()

    embeddings = embedding_service.embed_documents(chunks)

    repository = ChromaRepository()

    ids = repository.save_documents(chunks, embeddings)

    print(f"Stored {len(ids)} vectors.")


if __name__ == "__main__":
    main()    