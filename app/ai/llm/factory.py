from app.ai.llm.ollama_llm import OllamaLLM


class LLMFactory:

    @staticmethod
    def create():

        return OllamaLLM()