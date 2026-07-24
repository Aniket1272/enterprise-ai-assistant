from app.services.rag_service import RAGService


def main():

    rag = RAGService()

    question = input("Ask: ")

    answer = rag.ask(question)

    print("\n")
    print("=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(answer)


if __name__ == "__main__":
    main()