import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from src.ui import *
from src.funcs import *
from src.s3 import *

# load .env file
load_dotenv()

# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="SpotipyNX", page_icon="💥", layout="wide"
)
st.image("src/img/home_banner_v4.jpeg")

# ---*--- Init Session State ---*---
if "spotify_oauth" not in st.session_state:
    st.session_state.spotify_oauth = False
if "send_network_email" not in st.session_state:
    st.session_state.send_network_email = False
if "liked_songs_df" not in st.session_state:
    st.session_state.liked_songs_df = pd.DataFrame()
if "top_songs_df" not in st.session_state:
    st.session_state.top_songs_df = pd.DataFrame()

# ---*--- Sidebar Setup ---*---
add_logo()
sidebar()

# ---*--- Showcase Features ---*---
col1, col2, col3, col4, col5 = st.columns(5)

with col2:
   st.markdown("<h3 style='text-align: center;'>Explore Stats</h3>", unsafe_allow_html=True)
   st.image("./src/img/explorer_feature.png")

with col3:
   st.markdown("<h3 style='text-align: center;'>Generate Networks</h3>", unsafe_allow_html=True)
   st.image("./src/img/graph_feature.png")

with col4:
   st.markdown("<h3 style='text-align: center;'>Download Tables</h3>", unsafe_allow_html=True)
   st.image("./src/img/download_feature.png")


# ---*--- Streamlit WebApp Footer ---*---
st.markdown("---")
st.write(
    "Share on social media with the hashtag [#ccbda2023spotipyNX](https://twitter.com/) !"
)


# ---*---  ---*---
