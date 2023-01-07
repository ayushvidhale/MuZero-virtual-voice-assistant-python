import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="MuZero",page_icon=":cat:",layout="wide")
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottie("https://assets3.lottiefiles.com/private_files/lf30_fah4ouxp.json")
lottie_code = load_lottie("https://assets7.lottiefiles.com/packages/lf20_knnirj9a.json")
# # header section
# with st.container():
# # st.subheader("")-->medium
#   st.title("MuZero")#-->large
#   st.write("welcome to virtual assitant")
  
with st.container():
   one_column, two_column = st.columns((1,2))
   with one_column:
    st_lottie(lottie_code, height=300, key = "coding")
   with two_column:
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">MuZero</p>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Welcome to Virtual Assistant!!</p>', unsafe_allow_html=True)
st_lottie(lottie_coding, height=300, key = "code")
