import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
from dotenv import load_dotenv
from utils.ui import *

# load .env file
load_dotenv()

# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
add_logo()
sidebar()

st.image("utils/img/spotify_banner.jpeg")

button_spotify_oauth = st.button("Spotify OAuth")

# ---*--- Trigger Spotify OAuth ---*---
if button_spotify_oauth:
    try:
        scope = ["user-library-read", "user-top-read", "user-read-recently-played"]
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        saved_tracks_results = spotify.current_user_saved_tracks()
        saved_tracks = saved_tracks_results['items']

        st.success('Successful Spotify Authentication!', icon="✅")
        time.sleep(0.69) # small wait before releasing balloons
        st.balloons()
        st.write(
                "Your most recent saved songs:"
            )
        for idx, item in enumerate(saved_tracks[:20]):
            track = item['track']
            track_uri = track["uri"]
            st.write(
                f"{idx+1}. {track['name']}"
            )

    except Exception as e:
        print(e)


# ---*--- Streamlit WebApp Footer ---*---

st.markdown("---")
st.write(
    "Share on social media with the hashtag [#ccbda2023spotipyNX](https://twitter.com/) !"
)
