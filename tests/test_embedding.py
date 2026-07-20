from app.ai.embeddings.factory import EmbeddingFactory


def main():

    embedding = EmbeddingFactory.create()

    vector = embedding.embed_query(
        "What is Java?"
    )

    print(f"Dimension : {len(vector)}")
    print(vector[:10])


if __name__ == "__main__":
    main()