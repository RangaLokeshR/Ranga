from ai.engine.base_engine import BaseEngine
from ai.clients.gemini_client import GeminiClient


class GeminiEngine(BaseEngine):

    def __init__(self):
        self.client = GeminiClient()

    def ask(self, prompt: str) -> str:
        return self.client.generate(prompt)

    def is_available(self) -> bool:
        return True

    def model_name(self) -> str:
        return "Gemini 2.5 Flash"