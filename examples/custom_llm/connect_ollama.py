from hivemind import HiveMind, Agent, LLM
import requests

# Function to interact with the Ollama API
def ollama_llm(prompt: str, model: str = "llama3.1") -> str:
    """
    A custom LLM function that interacts with the Ollama API for local LLM inference.

    Args:
        prompt (str): The input prompt for the LLM.
        model (str): The Ollama model to use. Defaults to "llama3.1".

    Returns:
        str: The generated response from the Ollama model.
    """
    # Ollama API endpoint
    url = "http://localhost:11434/api/generate"
    
    # Payload for the API request
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        result = response.json()
        return result.get("response", "").strip()

    except requests.exceptions.RequestException as e:
        print(f"Error calling Ollama API: {e}")
        return f"An error occurred while generating the response: {e}"

# Register the Ollama LLM
LLM.register(name="ollama_llama3.1", function=lambda prompt: ollama_llm(prompt, model="llama3.1"))

# Initialize HiveMind
hivemind = HiveMind(verbose=True)

# Create a poem generator agent
hivemind.create_agent(
    name="poem_generator",
    backstory="An agent skilled in the art of poetry, tasked with generating beautiful verses.",
    instructions="Generate a short poem based on the user's input. Use creative and evocative language.",
    tool_names=[],  # No tools needed for this agent
    model_name="ollama_llama3.1",  # Use the registered Ollama model
    max_retries=3
)

# Example interaction with the poem generator agent
if __name__ == "__main__":
    print("Welcome to the Poem Generator! Share a theme, and I shall craft a poem for thee.")
    while True:
        user_input = input("\nTheme: ")
        if user_input.lower() in ["exit", "quit", "farewell"]:
            print("Farewell, dear poet! May your verses forever inspire.")
            break

        # Execute the task with the poem generator agent
        response = hivemind.run_agent("poem_generator", {"user_input": user_input})
        print(f"\nPoem:\n{response}")