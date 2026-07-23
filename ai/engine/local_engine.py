from ai.engine.base_engine import BaseEngine


class LocalEngine(BaseEngine):

    def ask(self, prompt: str) -> str:
        return "Local AI is not connected yet."

    def is_available(self) -> bool:
        return False

    def model_name(self) -> str:
        return "Local AI"