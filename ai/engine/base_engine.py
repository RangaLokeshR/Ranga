from abc import ABC, abstractmethod


class BaseEngine(ABC):

    @abstractmethod
    def ask(self, prompt: str) -> str:
        """
        Send a prompt to the AI model
        and return the response.
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """
        Check whether the AI engine
        is available.
        """
        pass

    @abstractmethod
    def model_name(self) -> str:
        """
        Return the AI model name.
        """
        pass