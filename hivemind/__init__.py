from .agent import Agent
from .hive import HiveMind
from .tool import Tool
from .llm import LLM

from openai import Client
import os


openaiClient = Client()

def gpt_4o_mini_get_response(prompt: str) -> str:
    """
    Get completions from the OpenAI GPT-4o-mini model.
    
    Args:
        prompt (str): The input prompt for the model.
    
    Returns:
        str: The model's response.
    """
    try:
        response = openaiClient.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error interacting with OpenAI: {e}"

# Register the OpenAI GPT-4o-mini model in the LLM manager
LLM.register("openai-gpt-4o-mini", gpt_4o_mini_get_response)
