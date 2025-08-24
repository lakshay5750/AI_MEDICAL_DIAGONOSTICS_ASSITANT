
import requests

EURI_API_KEY = "euri-12bfc7d1e9278bcce9417af8c8fa3a6fd5c727d7e780af659a1caeec49cd7c24"##give your

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

    url = "https://api.euron.one/api/v1/euri/chat/completions"
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


