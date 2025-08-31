import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

EURI_API_KEY = os.getenv("EURI_API_KEY")
EURI_API_URL = os.getenv("EURI_API_URL", "https://api.euron.one/api/v1/euri/chat/completions")

def generate_completion(user_input):
    """
    Sends user_input (string) to the EURI API and returns the model response.
    """
    # Ensure user_input is a string
    if isinstance(user_input, list):
        # Join list elements into a single string
        user_input = " ".join(map(str, user_input))

    user_input = str(user_input).strip()  # remove extra spaces/newlines

    if not user_input:
        return "Input is empty"

    url = EURI_API_URL
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EURI_API_KEY}"
    }
    payload = {
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "model": "gpt-4.1-nano",
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print("DEBUG API RESPONSE:", data)  # optional, for debugging

    # Extract model output safely
    if "choices" in data and len(data["choices"]) > 0:
        return data["choices"][0]["message"]["content"].strip()
    else:
        return "No valid response from API"

# Example usage


