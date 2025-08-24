from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda

from tools.diagnosis_tool import ai_diagnose
from tools.symptom_checker import ai_check_symptoms
from tools.diet import diet_tool


class DiagnosticState(TypedDict):
    input: str
    symptoms: str
    diagnosis: str
    dietary_recommendations: str


def build_graph():
    graph = StateGraph(DiagnosticState)

    # Step 1: Check symptoms
    def symptom_step(state: DiagnosticState) -> DiagnosticState:
        symptoms = ai_check_symptoms(state["input"])
        if not symptoms or not isinstance(symptoms, str):
            symptoms = "unknown symptoms"  # fallback for safety
        return {
            "input": state["input"],
            "symptoms": symptoms,
            "diagnosis": state.get("diagnosis", ""),
            "dietary_recommendations": state.get("dietary_recommendations", "")
        }

    graph.add_node("symptom_check", RunnableLambda(symptom_step))

    # Step 2: Generate diagnosis
    def diagnosis_step(state: DiagnosticState) -> DiagnosticState:
        symptoms = state.get("symptoms") or "unknown symptoms"
        diagnosis = ai_diagnose(symptoms)
        if not diagnosis or not isinstance(diagnosis, str):
            diagnosis = "unknown diagnosis"
        return {
            "input": state["input"],
            "symptoms": symptoms,
            "diagnosis": diagnosis,
            "dietary_recommendations": state.get("dietary_recommendations", "")
        }

    graph.add_node("diagnosis", RunnableLambda(diagnosis_step))

    # Step 3: Generate dietary recommendations
    def dietary_recommendations_step(state: DiagnosticState) -> DiagnosticState:
        symptoms = state.get("symptoms") or "unknown symptoms"
        dietary_recommendations = diet_tool({"symptom_description": symptoms})
        return {
            "input": state["input"],
            "symptoms": symptoms,
            "diagnosis": state.get("diagnosis", ""),
            "dietary_recommendations": dietary_recommendations
        }

    graph.add_node("dietary_recommendations", RunnableLambda(dietary_recommendations_step))

    # Graph edges
    graph.set_entry_point("symptom_check")
    graph.add_edge("symptom_check", "diagnosis")
    graph.add_edge("diagnosis", "dietary_recommendations")
    graph.add_edge("dietary_recommendations", END)

    return graph.compile()
