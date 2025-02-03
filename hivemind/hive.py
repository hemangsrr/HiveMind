from typing import Dict, Any, List, Optional
from .agent import Agent
from .tool import Tool


class HiveMind:
    """
    Manages multiple AI agents, tools, and LLM models in a modular system.
    """

    def __init__(self, verbose: bool = False):
        """
        Initializes the HiveMind system.

        Args:
            verbose (bool): Whether to enable debug logging. Defaults to False.
        """
        self.agents: Dict[str, Agent] = {}
        self.tools: Dict[str, Tool] = {}
        self.verbose = verbose

    def register_tool(self, tool: Tool):
        """
        Registers a new tool into the HiveMind.

        Args:
            tool (Tool): The tool instance to register.
        """
        self.tools[tool.name] = tool
        if self.verbose:
            print(f"[HiveMind] Registered tool: {tool.name}")

    def create_agent(
        self,
        name: str,
        backstory: str,
        instructions: str,
        tool_names: Optional[List[str]] = None,
        model_name: str = "openai-gpt-4o-mini",
        max_retries: int = 3,
    ):
        """
        Creates and registers an agent in the HiveMind.

        Args:
            name (str): The agent's name.
            backstory (str): Description of the agent's purpose or role.
            instructions (str): Primary task instructions for the agent.
            tool_names (List[str], optional): List of tool names to assign to the agent.
            model_name (str): The model name for LLM processing.
            max_retries (int): Max retry attempts for self-correction.
        """
        assigned_tools = [self.tools[t] for t in tool_names] if tool_names else []
        agent = Agent(
            name=name,
            backstory=backstory,
            instructions=instructions,
            tools=assigned_tools,
            model_name=model_name,
            max_retries=max_retries,
            verbose=self.verbose,
        )
        self.agents[name] = agent

        if self.verbose:
            print(f"[HiveMind] Created agent: {name}")

    def run_agent(self, agent_name: str, inputs: Dict[str, Any]) -> str:
        """
        Executes a task by invoking the specified agent.

        Args:
            agent_name (str): Name of the agent to execute the task.
            inputs (Dict[str, Any]): Input parameters for the agent.

        Returns:
            str: The final response from the agent.
        """
        if agent_name not in self.agents:
            raise ValueError(f"Agent '{agent_name}' not found in HiveMind.")

        agent = self.agents[agent_name]

        if self.verbose:
            print(f"\n[HiveMind] Invoking agent: {agent.name} with input: {inputs}")

        response = agent.invoke(inputs)

        if self.verbose:
            print(f"\n[HiveMind] Agent Response: {response}")

        return response
