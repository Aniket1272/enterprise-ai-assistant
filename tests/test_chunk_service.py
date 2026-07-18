from app.chunking.chunk_service import ChunkService
from app.loaders.pdf_loader import PDFLoader


def main():

    text = PDFLoader.load("uploads/sample.pdf")

    chunk_service = ChunkService()

    chunks = chunk_service.split(text)

    print("=" * 60)

    print(f"Total Chunks: {len(chunks)}")

    print("=" * 60)

    for index, chunk in enumerate(chunks):

        print(f"\nChunk {index + 1}")

        print("-" * 40)

        print(chunk.page_content)

        print("-" * 40)


if __name__ == "__main__":

    main()