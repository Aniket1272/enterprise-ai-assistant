from app.chunking.chunk_service import ChunkService
from app.ai.embeddings.ollama_embedding import EmbeddingService
from app.loaders.pdf_loader import PDFLoader


def main():

    text = PDFLoader.load("uploads/sample.pdf")

    chunks = ChunkService().split(text)

    embeddings = EmbeddingService().embed_documents(chunks)

    print(f"Total Chunks : {len(chunks)}")

    print(f"Total Embeddings : {len(embeddings)}")

    print(f"Embedding Dimension : {len(embeddings[0])}")

    print()

    print(embeddings[0][:10])


if __name__ == "__main__":

    main()