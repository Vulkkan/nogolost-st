import streamlit as st
from streamlit_chat import message as st_message
import helper.rag as rag
from helper.key import API_TOKEN


st.title("💬 Nogolost Chat")

# # Require token
# if "api_token" not in st.session_state:
#     st.warning("⚠️ Please set your Hugging Face API token in the previous page.")
#     st.stop()

# Pass the token to RAG
rag.set_api_token(st.session_state.api_token)
# rag.set_api_token(API_TOKEN)

@st.cache_data
def load_data():
    return rag.chunkData("data/data.txt")

rag_data = load_data()

if "messages" not in st.session_state:
    st.session_state.messages = []

for i, message in enumerate(st.session_state.messages):
    st_message(message["content"], is_user=(message["role"] == "user"), key=f"message_{i}")

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st_message(prompt, is_user=True, key=f"user_{len(st.session_state.messages)}")

    response = rag.reply(prompt, rag_data)
    st_message(response, is_user=False, key=f"assistant_{len(st.session_state.messages)}")
    st.session_state.messages.append({"role": "assistant", "content": response})
