from ai.engine.gemini_engine import GeminiEngine
from ai.engine.local_engine import LocalEngine
from config.settings import AI_ENGINE


class EngineFactory:

    @staticmethod
    def create():

        if AI_ENGINE.lower() == "gemini":
            return GeminiEngine()

        elif AI_ENGINE.lower() == "local":
            return LocalEngine()

        else:
            raise ValueError("Unknown AI Engine")