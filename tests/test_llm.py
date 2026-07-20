from app.ai.llm.factory import LLMFactory



def main():
    llm = LLMFactory.create()

    response = llm.generate(
        "Explain me what is REST API in 2 lines."
    )

    print(response)


if __name__ == "__main__":
    main()    