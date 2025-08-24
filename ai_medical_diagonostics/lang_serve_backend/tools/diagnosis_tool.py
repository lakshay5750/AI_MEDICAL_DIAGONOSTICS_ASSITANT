from langchain.tools import tool
from utils.euri_client import generate_completion

def ai_diagnose(symptom_description):
    """Diagnose a medical condition based on the given symptom description."""
    message=[{
        "role":"user",
        "content":f"Diagnose the medical condition based on the following symptoms: {symptom_description}. Provide a brief explanation and provide next steps for the patient."
        }]
    return generate_completion(message)
