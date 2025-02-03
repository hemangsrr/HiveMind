from typing import Callable, Dict, Any, Optional
from langchain.tools import BaseTool

class Tool:
    """
    A flexible tool class that allows users to define their own tools in Python.
    It also supports LangChain tools as a base for seamless integration.
    """

    def __init__(
        self,
        name: str,
        function: Callable[..., Any],
        description: str = "A custom tool.",
        use_langchain: bool = False,
        langchain_tool: Optional[BaseTool] = None,
    ):
        """
        Initialize a tool.

        Args:
            name (str): The name of the tool.
            function (Callable): The function that defines the tool's behavior.
            description (str, optional): A description of what the tool does.
            use_langchain (bool, optional): Whether the tool is a LangChain tool.
            langchain_tool (BaseTool, optional): The LangChain tool instance if using LangChain.
        """
        self.name = name
        self.function = function
        self.description = description
        self.use_langchain = use_langchain
        self.langchain_tool = langchain_tool

    def run(self, *args, **kwargs) -> Any:
        """
        Execute the tool with the given arguments.

        Returns:
            Any: The output of the tool.
        """
        if self.use_langchain and self.langchain_tool:
            return self.langchain_tool.run(*args, **kwargs)
        elif not self.use_langchain:
            return self.function(*args, **kwargs)
        else:
            raise ValueError(f"Invalid tool configuration: LangChain specified, but no LangChain tool provided.")


    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the tool metadata to a dictionary.

        Returns:
            dict: A dictionary containing tool details.
        """
        return {
            "name": self.name,
            "description": self.description,
            "use_langchain": self.use_langchain,
            "function": self.function.__name__,  # function name for reference
            "langchain_tool": self.langchain_tool.__repr__() if self.langchain_tool else None,
        }

    def __repr__(self):
        return f"Tool(name={self.name}, use_langchain={self.use_langchain})"