from app.loaders.pdf_loader import PDFLoader
from app.processors.text_processor import TextProcessor
from app.chunking.chunk_service import ChunkService
from app.ai.embeddings.factory import EmbeddingFactory


def main():

    text = PDFLoader.load("uploads/sample.pdf")

    print("=" * 60)
    print("PDF Loaded")
    print("=" * 60)

    processed = TextProcessor().process(text)

    print("Text Processed")

    chunks = ChunkService().split(processed)

    print(f"Chunks Created : {len(chunks)}")

    embedding = EmbeddingFactory.create()

    vectors = embedding.embed_documents(chunks)

    print(f"Embeddings Generated : {len(vectors)}")

    print(f"Vector Dimension : {len(vectors[0])}")


if __name__ == "__main__":
    main()