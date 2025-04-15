import streamlit as st
from res.styles import custom_css


st.markdown(custom_css(), unsafe_allow_html=True)

st.markdown(f"<h1 class='colored-subtitle''>Configuration</h1>", unsafe_allow_html=True)
st.write('')

# --------------------- Model & key --------------------- #
model_selection = st.selectbox("Select model", [
    'meta-llama/llama-4-maverick',
    'openai/gpt-3.5-turbo',

    'deepseek/deepseek-r1-distill-llama-70b',
    'meta-llama/llama-4-scout',

    'deepseek/deepseek-r1-distill-llama-8b', 
    'deepseek/deepseek-r1-distill-qwen-1.5b',

    'meta-llama/llama-3.2-1b-instruct',
    'mistral/ministral-8b',
])
token_input = st.text_input("Enter the corresponding API key", placeholder='sk-or-v1-')


# --------------------- Set parameters --------------------- #
if st.button("Proceed", type="primary"):
    if token_input and model_selection:
        st.session_state.api_token = token_input
        st.session_state.model = model_selection

        st.success("Good to go!")

        # Defer switch_page until after token is saved
        st.switch_page("pages/2_💬_Nogolost_Chat.py")
    else:
        st.warning("⚠️ Please enter a token to proceed!")

