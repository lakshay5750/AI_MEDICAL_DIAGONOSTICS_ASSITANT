import streamlit as st
import requests

st.title("AI Medical Diagnostics")
st.write("Welcome to the AI Medical Diagnostics application!")
st.text("Please enter your symptoms below:")
symptoms_input = st.text_area("Symptoms")

if st.button("Submit"):
    
    
    try:
        response = requests.post(
            "https://ai-medical-diagonostics-assitant-3.onrender.com/diagnostics/invoke",
             json={
                "input": {
                    "input": symptoms_input,
                    "symptoms": "",
                    "diagnosis": "",
                    "dietary_recommendations": ""
                }
            },  # ✅ send the full object
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()  # Raise an error for HTTP errors
        data = response.json()
        st.write(response.status_code)
        st.write(response.text)
        st.write(response.json()) 
        st.write("Raw JSON from backend:", data)
        st.write("Debug raw json: ", data)
        st.subheader("Detected Symptoms:")
        st.write(data.get("symptoms", "N/A"))
        st.subheader("Diagnosis:")
        st.write(data.get("diagnosis", "N/A"))
        st.subheader("Dietary Recommendations:")
        st.write(data.get("dietary_recommendations", "N/A"))
    except Exception as e:
        st.write("Error occurred: ", e)

        
