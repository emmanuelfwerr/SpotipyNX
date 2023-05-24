import streamlit as st
from src.ui import *

# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
#st.image("src/img/home_banner.png")
add_logo()
sidebar()

#st.checkbox("Use container width", value=False, key="use_container_width")
st.markdown("<h3 style='text-align: center; color: white;'>Recent Liked Songs Raw DataFrame</h3>", unsafe_allow_html=True)
liked_songs_df = st.session_state.liked_songs_df
st.dataframe(liked_songs_df)

st.markdown("<h3 style='text-align: center; color: white;'>Current Top Songs Raw DataFrame</h3>", unsafe_allow_html=True)
top_songs_df = st.session_state.top_songs_df
st.dataframe(top_songs_df)