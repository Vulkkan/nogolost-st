import streamlit as st
from res.styles import custom_css


st.set_page_config(page_title="Nogolost", layout="wide")
st.markdown(custom_css(), unsafe_allow_html=True)

st.markdown(f"<h1 class='dash-title''>Nogolost</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 class='colored-text''>Your travel virtual assistant</h1>", unsafe_allow_html=True)


st.write(' '); st.write(' '); st.write(' '); st.write(' ')
st.write(' '); st.write(' '); st.write(' '); st.write(' ')

# --------------------- Go --------------------- #
go = st.button('Proceed', type='primary')

if go:
    st.switch_page('pages/1_🏁_Set_API_Token.py')
