import streamlit as st
from helper.key import API_TOKEN

st.title("Set Hugging Face API Token")

# Prompt user for the token
token_input = st.text_input("Enter your Hugging Face API token:", type="password")

# Save the token only if button is clicked
if st.button("Proceed", type="primary"):
    if token_input:
        API_TOKEN = token_input
        st.session_state.api_token = token_input
        st.success("API token saved successfully!")

        # 🔁 Defer switch_page until after token is saved
        st.switch_page("pages/2_💬_Nogolost_Chat.py")
    else:
        st.warning("⚠️ Please enter a token before proceeding.")
