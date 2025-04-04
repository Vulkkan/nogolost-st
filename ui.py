import streamlit as st
from res.styles import custom_css


st.set_page_config(page_title="Nogolost", layout="wide")

st.title("Welcome to Nogolost RAG App")

st.markdown(custom_css(), unsafe_allow_html=True)


go = st.button('Proceed', type='primary')

if go:
    st.switch_page('pages/1_🏁_Set_API_Token.py')
