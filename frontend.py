import streamlit as st
import requests

# Since both processes run in the same container, use localhost!
BACKEND_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 LangGraph Agent UI")
st.caption("Live Production Agent hosted on AWS Fargate")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask your agent anything..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*Agent is thinking...*")
        
        try:
            # Hit your FastAPI endpoint
            response = requests.post(BACKEND_URL, json={"message": prompt}, timeout=30)
            
            if response.status_code == 200:
                # Adjust key below matching your FastAPI response schema (e.g., response.json()["response"])
                ai_response = response.json().get("response", response.text)
                message_placeholder.markdown(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            else:
                error_msg = f"Backend Error: Status code {response.status_code}"
                message_placeholder.markdown(error_msg)
        except Exception as e:
            message_placeholder.markdown(f"Failed to connect to backend: {str(e)}")