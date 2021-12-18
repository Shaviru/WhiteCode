import streamlit as st
from streamlit_ace import *


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.alphacoders.com/116/thumb-1920-1169862.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://images.alphacoders.com/116/thumb-1920-1169862.jpg")
    }S
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color:White; '>WhiteCode Editor</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<h1 style='text-align: center;'>Adjust the parameters of your Code Editor</h1>", unsafe_allow_html=True)
st.sidebar.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)
lang = ['python', 'java', 'html']
lang_var = st.sidebar.selectbox('Select the programming language', lang)

input_style = '<p style="font-family:sans-serif; color:White; font-size: 30px;">Input your code here:</p>'
st.markdown(input_style, unsafe_allow_html=True)
code = st_ace(language = lang_var,
theme='vibrant_ink', wrap=False, show_print_margin=True,
keybinding="vscode", show_gutter=True, auto_update=True, 
height=300)
