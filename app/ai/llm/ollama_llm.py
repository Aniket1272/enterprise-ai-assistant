from langchain_ollama import ChatOllama
from app.core.settings import settings
from app.ai.llm.base_llm import BaseLLM


class OllamaLLM(BaseLLM):

    def __init__(self):
        
        self.model = ChatOllama(
            model=settings.CHAT_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0,
        )


    def generate(self, prompt: str):
        
        responses = self.model.invoke(prompt)

        return responses.content

