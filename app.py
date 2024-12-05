import streamlit as st
import google.generativeai as genai

# Configure the API key
# API_KEY = "AIzaSyBUv8wjsis3NuLK9O9nmfu5O2ndELvMGFA"
genai.configure(api_key="AIzaSyBUv8wjsis3NuLK9O9nmfu5O2ndELvMGFA")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title of the app
st.title("Interactive Chatbot")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for user to enter their message
if prompt := st.chat_input("Type your message here..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate response from Gemini API
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    # Display assistant response
    assistant_response = response.text
    st.chat_message("assistant").markdown(assistant_response)
    
    # Append assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})