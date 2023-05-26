import os
import time
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
from src.funcs import *


def display_banner():
    st.image("img/home_banner.png")

def set_state_if_absent(key, value):
    if key not in st.session_state:
        st.session_state[key] = value

def set_initial_state():
    set_state_if_absent("username", "Provide a Twitter username")
    set_state_if_absent("result", None)
    set_state_if_absent("haystack_started", False)

def reset_results(*args):
    st.session_state.result = None

def sidebar():
    if "spotify_oauth" not in st.session_state:
        st.session_state.spotify_oauth = False

    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Connect Spotify Account using the `Spotify OAuth` button\n"
            "2. Wait briefly while we fetch and process your data\n"
            "3. Enjoy 🤗\n"
        )
        button_spotify_oauth = st.button("Spotify OAuth")
        
        if button_spotify_oauth:
            st.session_state.spotify_oauth = True

            try:
                # ---*--- Trigger Spotify OAuth ---*---
                scope = ["user-library-read", "user-top-read", "user-read-recently-played"]

                # ---*--- Fix .cache inside Docker ---*---
                '''cache_dir = '.cache'
                if not os.path.exists(cache_dir):
                    os.makedirs(cache_dir)
                os.chmod(cache_dir, 0o700)'''

                # ---*---  ---*---
                st.session_state.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

                liked_tracks_results = st.session_state.spotify.current_user_saved_tracks()
                top_tracks_results = st.session_state.spotify.current_user_top_tracks()

                st.session_state.liked_songs_df = parse_liked_tracks_DF(liked_tracks_results)
                st.session_state.top_songs_df = parse_top_tracks_DF(top_tracks_results)

                # Horay!
                time.sleep(0.69) # small wait before releasing balloons
                st.balloons()

            except Exception as e:
                print(e)
        
        if st.session_state.spotify_oauth:
            st.success('Successful Spotify OAuth!', icon="✅")

        st.markdown("---")
        st.markdown(
            "## How this works\n"
            "This app was built with [Streamlit](https://streamlit.io) using the"
            " [Spotify Web API](https://developer.spotify.com/documentation/web-api) and is hosted on [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)"
        )
        st.markdown("---")
        st.markdown("**Take results with a grain of** 🧂\n\n"
            "There's a lot that can be improved to make this app better.\n\n"
            "For more on how this was built, instructions to run locally and to contribute: [visit GitHub](https://github.com/emmanuelfwerr/SpotipyNX/tree/main)"
        )
        st.markdown("---")


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "SpotipyNX";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 69px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )