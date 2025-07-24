import streamlit as st
import google.generativeai as genai

# 🔐 Your API Key
API_KEY = "AIzaSyBsWBdMazOqB6Nm9J6nLSVGqbfRUdPuydI"  # Replace this with your actual key
import streamlit as st
import google.generativeai as genai


genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")

st.title("Aaroh AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask Aaroh AI"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.markdown(
    """
    <style>
    /* Change font */
    html, body, [class*="css"]  {
        font-family: 'Courier New', monospace;
    }
    /* Change font size */
    .css-18e3th9 {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
