import streamlit as st
from streamlit_chat import message as st_message

import helper.rag as rag
# import local.helper.rag as rag


st.title("Nogolost Test")

# Load the data only once
@st.cache_data
def load_data():
    return rag.chunkData("data/data.txt")

rag_data = load_data()


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with unique keys for each message
for i, message in enumerate(st.session_state.messages):
    st_message(message["content"], is_user=(message["role"] == "user"), key=f"message_{i}")


# Handle user input
if prompt := st.chat_input():
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message with a unique key and custom avatar
    st_message(
        prompt, 
        is_user=True, 
        key=f"user_{len(st.session_state.messages)}"
    )

    response = rag.reply(prompt, rag_data)

    # Display bot response once with a unique key and custom avatar
    st_message(response, is_user=False, key=f"assistant_{len(st.session_state.messages)}")

    # Append bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

