
# HiveMind

HiveMind is a modular system for managing multiple AI agents, tools, and LLM models. It allows you to create, register, and orchestrate agents that can perform tasks using a variety of tools and language models. The system is designed to be flexible, extensible, and easy to integrate into your projects.


## Features
- Agent Management: Create and manage AI agents with unique backstories, instructions, and tools.
- Tool Integration: Register and use custom tools or LangChain tools seamlessly.
- LLM Flexibility: Register and use different LLM models (e.g., OpenAI GPT, local models) for inference.
- Self-Correction: Agents can verify and self-correct their responses for improved accuracy.
- Verbose Logging: Enable detailed logging for debugging and monitoring.

## Installation

You can install HiveMind via pip:
```python
pip install git+https://github.com/hemangsrr/hivemind.git
```

## Usage
Creating a HiveMind Instance

```python
from hivemind import HiveMind

hivemind = HiveMind(verbose=True)
```

### Registering Tools
```python
from hivemind import Tool

def custom_tool_function(input_data):
    # Your custom logic here
    return "Processed data"

custom_tool = Tool(name="custom_tool", function=custom_tool_function, description="A custom tool for processing data.")
hivemind.register_tool(custom_tool)
```

## Creating an Agent
```python
hivemind.create_agent(
    name="data_processor",
    backstory="An agent designed to process data using custom tools.",
    instructions="Process the input data and return the result.",
    tool_names=["custom_tool"],
    model_name="openai-gpt-4o-mini",
    max_retries=3
)
```

## Running an agent

```python
inputs = {"custom_tool": {"data": "example data"}}
response = hivemind.run_agent("data_processor", inputs)
print(response)
```

## Registering an LLM
```python
from hivemind import LLM

def custom_llm(prompt: str) -> str:
    # Your custom LLM logic here
    return "Generated response"

LLM.register(name="custom_llm", function=custom_llm)
```