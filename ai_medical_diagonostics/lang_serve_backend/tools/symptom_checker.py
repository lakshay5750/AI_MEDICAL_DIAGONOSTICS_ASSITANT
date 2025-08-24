from langchain.tools import tool
from utils.euri_client import generate_completion


@tool
def ai_check_symptoms(symptoms: str) -> str:
    """this tool analyse the user's symptoms and provides a which type of medical condition it could be"""
    message=[{
        "role":"user",
        "content":f"Diagnose the medical condition based on the following symptoms: {symptoms}. Provide a brief explanation and provide next steps for the patient."
    }]
    return generate_completion(message)
