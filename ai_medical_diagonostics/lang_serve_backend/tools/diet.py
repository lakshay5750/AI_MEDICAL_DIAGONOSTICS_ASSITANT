from langchain.tools import tool
from utils.euri_client import generate_completion

@tool
def diet_tool(symptom_description: str) -> str:
    """this tool provides dietary recommendations based on the user's needs"""
    message=[{
        "role":"user",
        "content":f"Provide dietary recommendations based on the following symptoms: {symptom_description}. Include meal ideas and nutritional information."
    }]
    return generate_completion(message)
