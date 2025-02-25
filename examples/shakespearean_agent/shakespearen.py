from hivemind import HiveMind, LLM
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

# Initialize HiveMind
hivemind = HiveMind(verbose=True)

# Create a Shakespearean agent
hivemind.create_agent(
    name="shakespearean_bard",
    backstory="An agent well-versed in the works of William Shakespeare, tasked with conversing in Old English.",
    instructions="Thou shalt respond to all queries in the style of William Shakespeare, using Old English and poetic flair.",
    tool_names=[],  # No tools needed for this agent
    model_name="openai-gpt-4o-mini", 
    max_retries=3
)

# Example conversation with the Shakespearean agent
if __name__ == "__main__":
    print("Welcome to the Shakespearean Bard! Speak, and thou shalt receive wisdom in the tongue of the Bard.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "farewell"]:
            print("Farewell, noble soul! May thy days be filled with sonnets and joy.")
            break

        # Execute the task with the Shakespearean agent
        response = hivemind.run_agent("shakespearean_bard", {"user_input": user_input})
        print(f"\nBard: {response}")