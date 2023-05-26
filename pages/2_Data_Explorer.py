import streamlit as st
from src.ui import *
from src.funcs import *

# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
#st.image("src/img/home_banner.png")
add_logo()
sidebar()

# ---*--- Liked Songs Raw DataFrame ---*---
st.markdown("<h3 style='text-align: center;'>Recent Liked Songs Raw DataFrame</h3>", unsafe_allow_html=True)
liked_songs_df = st.session_state.liked_songs_df
st.dataframe(liked_songs_df)

# enable download
liked_songs_csv = convert_df(liked_songs_df)

st.download_button(
   "Download Liked Songs DataFrame",
   liked_songs_csv,
   "liked_songs.csv",
   "text/csv",
   key='download-liked-songs-csv'
)

# ---*--- Top Songs Raw DataFrame ---*---
st.markdown("<h3 style='text-align: center;'>Current Top Songs Raw DataFrame</h3>", unsafe_allow_html=True)
top_songs_df = st.session_state.top_songs_df
st.dataframe(top_songs_df)

# enable download
top_songs_csv = convert_df(top_songs_df)

st.download_button(
   "Download Top Songs DataFrame",
   top_songs_csv,
   "top_songs.csv",
   "text/csv",
   key='download-top-songs-csv'
)


# ---*--- Streamlit WebApp Footer ---*---
st.markdown("---")
st.write(
    "Share on social media with the hashtag [#ccbda2023spotipyNX](https://twitter.com/) !"
)