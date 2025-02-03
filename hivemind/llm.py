from typing import Callable, Dict, Any

class LLM:
    """
    A flexible LLM manager that allows users to register and use different models.

    Users can define their own LLMs (API calls, local models, etc.) and register them 
    with a unique name. The system will then use the registered model for inference.
    """

    _registry: Dict[str, Callable[[str], str]] = {}

    @classmethod
    def register(cls, name: str, function: Callable[[str], str]) -> None:
        """
        Register a new LLM with a given name.

        Args:
            name (str): The name of the LLM.
            function (Callable[[str], str]): A function that takes a prompt as input and returns a response.
        """
        cls._registry[name] = function

    @classmethod
    def get(cls, name: str) -> Callable[[str], str]:
        """
        Retrieve an LLM function by name.

        Args:
            name (str): The name of the registered LLM.

        Returns:
            Callable[[str], str]: The function that generates a response from the LLM.

        Raises:
            ValueError: If the LLM name is not found in the registry.
        """
        if name not in cls._registry:
            raise ValueError(f"LLM '{name}' is not registered. Available models: {list(cls._registry.keys())}")
        return cls._registry[name]

    @classmethod
    def list_models(cls) -> Dict[str, Callable[[str], str]]:
        """Returns a list of all registered LLMs."""
        return list(cls._registry.keys())

    @classmethod
    def infer(cls, name: str, prompt: str) -> str:
        """
        Run inference using the specified LLM.

        Args:
            name (str): The name of the registered LLM.
            prompt (str): The input text.

        Returns:
            str: The generated response.
        """
        try:
            llm_function = cls.get(name)
            return llm_function(prompt)
        except Exception as e:
            raise RuntimeError(f"Error during inference with LLM '{name}': {str(e)}")