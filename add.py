import streamlit as st
import google.generativeai as genai

# Custom Instruction - Social Challenge ke liye
CUSTOM_INSTRUCTION = "You are an authentic, supportive friend. Help the user reflect on their day with empathy and positivity."

st.set_page_config(page_title="Personal Gemini Journal")
st.title("Personal Gemini Journal 🔒")

# Simple Auth (Firebase ki jagah simple login for demo)
username = st.text_input("Enter your name to login")
if not username:
    st.stop()

st.write(f"Welcome {username}! Write your journal")

journal = st.text_area("How was your day today?")
if st.button("Get AI Reflection"):
    # Gemini call (AI Studio API Key yaha lagegi)
    genai.configure(api_key="YOUR_API_KEY")
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=CUSTOM_INSTRUCTION)
    response = model.generate_content(journal)
    st.success(response.text)

st.caption("Secure | Authentic | Deployed on Cloud Run")
