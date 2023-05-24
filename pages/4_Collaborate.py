import streamlit as st
from src.ui import *

# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
#st.image("src/img/home_banner.png")
add_logo()
sidebar()

st.write("page 4 collaborate")


# ---*--- Streamlit WebApp Footer ---*---
st.markdown("---")
st.write(
    "Share on social media with the hashtag [#ccbda2023spotipyNX](https://twitter.com/) !"
)