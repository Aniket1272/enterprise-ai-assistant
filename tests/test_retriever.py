from app.retriever.retriever_service import RetrieverService


def main():

    retriever = RetrieverService()

    result = retriever.retrieve(
        "What is this document about?"
    )

    print(result)


if __name__ == "__main__":
    main()