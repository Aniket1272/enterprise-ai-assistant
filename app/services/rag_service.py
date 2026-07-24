from app.ai.llm.factory import LLMFactory
from app.prompts.prompt_builder import PromptBuilder
from app.retriever.retriever_service import RetrieverService


class RAGService:

    def __init__(self):

        self.retriever = RetrieverService()
        self.llm = LLMFactory.create()


    def ask(self, question: str):

        context = self.retriever.retrieve_context(question)

        prompt = PromptBuilder.build(
            context,
            question
        )  

        return self.llm.generate(prompt)  