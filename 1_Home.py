import time
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
from dotenv import load_dotenv
from src.ui import *
from src.funcs import *
from src.s3 import *

# load .env file
load_dotenv()

# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
add_logo()
sidebar()

st.image("src/img/home_banner_v4.jpeg")

button_spotify_oauth = st.button("Spotify OAuth")

# ---*---  ---*---
if "liked_songs_df" not in st.session_state:
    st.session_state.liked_songs_df = pd.DataFrame()
if "top_songs_df" not in st.session_state:
    st.session_state.top_songs_df = pd.DataFrame()

# ---*--- Trigger Spotify OAuth ---*---
if button_spotify_oauth:
    try:
        scope = ["user-library-read", "user-top-read", "user-read-recently-played"]
        st.session_state.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        st.success('Successful Spotify Authentication!', icon="✅")

        #test_s3 = uploadS3('.gitignore', f'test_{str(time.time())}.txt')
        #sendEmail2(test_s3, 'adriamedina@outlook.es' ,'New file in the bucket!')

        # ---*--- Fetch Songs Data ---*---
        @st.cache_data
        def parse_liked_tracks_DF(liked_tracks_results: object, n: int=20) -> pd.DataFrame():
            """
            Fetch a user's saved songs using the spotify client.

            Args:
                spotify: A Spotipy object used to interact with the Spotify API

            Returns:
                liked_tracks_DF: A Pandas DataFrame with tracks and their metadata
            """
            liked_tracks = liked_tracks_results['items']

            # ---*--- Liked Songs <3 ---*---

            liked_songs_uris = []
            liked_songs_df = pd.DataFrame(
                columns=[
                    "track_name", "added_date",
                    "track_release_date", "track_popularity",
                    "af_danceability", "af_energy", "af_key",
                    "af_loudness", "af_mode", "af_speechiness",
                    "af_acousticness", "af_instrumentalness",
                    "af_liveness", "af_valence", "af_tempo", "af_type",
                    "af_duration", "af_time_signature", "main_artist_uri",
                    "main_artist_name", "main_artist_followers",
                    "main_artist_genres", "main_artist_popularity"
                ]
            )

            for idx, item in enumerate(liked_tracks[:n]):
                track = item['track']
                track_uri = track["uri"]

                liked_songs_uris.append(track_uri)

                liked_songs_df.loc[track_uri, "added_date"] = item["added_at"]
                liked_songs_df.loc[track_uri, "track_name"] = track["name"]
                liked_songs_df.loc[track_uri, "track_release_date"] = track["album"]["release_date"]
                liked_songs_df.loc[track_uri, "track_popularity"] = track["popularity"]

                audio_features = st.session_state.spotify.audio_features([track_uri])[0] #function requires a list

                liked_songs_df.loc[track_uri, "af_danceability"] = audio_features["danceability"]
                liked_songs_df.loc[track_uri, "af_energy"] = audio_features["energy"]
                liked_songs_df.loc[track_uri, "af_key"] = audio_features["key"]
                liked_songs_df.loc[track_uri, "af_loudness"] = audio_features["loudness"]
                liked_songs_df.loc[track_uri, "af_mode"] = audio_features["mode"]
                liked_songs_df.loc[track_uri, "af_speechiness"] = audio_features["speechiness"]
                liked_songs_df.loc[track_uri, "af_acousticness"] = audio_features["acousticness"]
                liked_songs_df.loc[track_uri, "af_instrumentalness"] = audio_features["instrumentalness"]
                liked_songs_df.loc[track_uri, "af_liveness"] = audio_features["liveness"]
                liked_songs_df.loc[track_uri, "af_valence"] = audio_features["valence"]
                liked_songs_df.loc[track_uri, "af_tempo"] = audio_features["tempo"]
                liked_songs_df.loc[track_uri, "af_type"] = audio_features["type"]
                liked_songs_df.loc[track_uri, "af_duration"] = audio_features["duration_ms"]
                liked_songs_df.loc[track_uri, "af_time_signature"] = audio_features["time_signature"]

                main_artist_uri = track["artists"][0]["uri"]
                liked_songs_df.loc[track_uri, "main_artist_uri"] = main_artist_uri
                main_artist = st.session_state.spotify.artist(main_artist_uri)
                liked_songs_df.loc[track_uri, "main_artist_name"] = main_artist["name"]
                liked_songs_df.loc[track_uri, "main_artist_followers"] = main_artist["followers"]["total"]
                liked_songs_df.loc[track_uri, "main_artist_genres"] = main_artist["genres"]
                liked_songs_df.loc[track_uri, "main_artist_popularity"] = main_artist["popularity"]

            return liked_songs_df


        @st.cache_data
        def parse_top_tracks_DF(top_tracks_results: object, n: int=20) -> pd.DataFrame():
            """
            Fetch a user's top songs using the spotify client.

            Args:
                spotify: A Spotipy object used to interact with the Spotify API

            Returns:
                top_tracks_DF: A Pandas DataFrame with tracks and their metadata
            """
            top_tracks = top_tracks_results['items']

            # ---*--- Top Songs ^ ---*---

            top_songs_uris = []
            top_songs_df = pd.DataFrame(
                columns=[
                    "track_name",
                    "track_release_date", "track_popularity",
                    "af_danceability", "af_energy", "af_key",
                    "af_loudness", "af_mode", "af_speechiness",
                    "af_acousticness", "af_instrumentalness",
                    "af_liveness", "af_valence", "af_tempo", "af_type",
                    "af_duration", "af_time_signature", "main_artist_uri",
                    "main_artist_name", "main_artist_followers",
                    "main_artist_genres", "main_artist_popularity"
                ]
            )

            for idx, item in enumerate(top_tracks[:]):
                track = item
                track_uri = track["uri"]

                top_songs_uris.append(track_uri)

                top_songs_df.loc[track_uri, "track_name"] = track["name"]
                top_songs_df.loc[track_uri, "track_release_date"] = track["album"]["release_date"]
                top_songs_df.loc[track_uri, "track_popularity"] = track["popularity"]

                audio_features = st.session_state.spotify.audio_features([track_uri])[0] #function requires a list

                top_songs_df.loc[track_uri, "af_danceability"] = audio_features["danceability"]
                top_songs_df.loc[track_uri, "af_energy"] = audio_features["energy"]
                top_songs_df.loc[track_uri, "af_key"] = audio_features["key"]
                top_songs_df.loc[track_uri, "af_loudness"] = audio_features["loudness"]
                top_songs_df.loc[track_uri, "af_mode"] = audio_features["mode"]
                top_songs_df.loc[track_uri, "af_speechiness"] = audio_features["speechiness"]
                top_songs_df.loc[track_uri, "af_acousticness"] = audio_features["acousticness"]
                top_songs_df.loc[track_uri, "af_instrumentalness"] = audio_features["instrumentalness"]
                top_songs_df.loc[track_uri, "af_liveness"] = audio_features["liveness"]
                top_songs_df.loc[track_uri, "af_valence"] = audio_features["valence"]
                top_songs_df.loc[track_uri, "af_tempo"] = audio_features["tempo"]
                top_songs_df.loc[track_uri, "af_type"] = audio_features["type"]
                top_songs_df.loc[track_uri, "af_duration"] = audio_features["duration_ms"]
                top_songs_df.loc[track_uri, "af_time_signature"] = audio_features["time_signature"]

                main_artist_uri = track["artists"][0]["uri"]
                top_songs_df.loc[track_uri, "main_artist_uri"] = main_artist_uri
                main_artist = st.session_state.spotify.artist(main_artist_uri)
                top_songs_df.loc[track_uri, "main_artist_name"] = main_artist["name"]
                top_songs_df.loc[track_uri, "main_artist_followers"] = main_artist["followers"]["total"]
                top_songs_df.loc[track_uri, "main_artist_genres"] = main_artist["genres"]
                top_songs_df.loc[track_uri, "main_artist_popularity"] = main_artist["popularity"]

            return top_songs_df

        liked_tracks_results = st.session_state.spotify.current_user_saved_tracks()
        top_tracks_results = st.session_state.spotify.current_user_top_tracks()

        st.session_state.liked_songs_df = parse_liked_tracks_DF(liked_tracks_results)
        st.session_state.top_songs_df = parse_top_tracks_DF(top_tracks_results)

        time.sleep(0.69) # small wait before releasing balloons
        st.balloons()


    except Exception as e:
        print(e)

col1, col2, col3, col4, col5 = st.columns(5)
with col2:
   st.markdown("<h3 style='text-align: center; color: white;'>Explore Stats</h3>", unsafe_allow_html=True)
   st.image("./src/img/explorer_feature.jpeg")

with col3:
   st.markdown("<h3 style='text-align: center; color: white;'>Generate Networks</h3>", unsafe_allow_html=True)
   st.image("./src/img/graph_feature.png")

with col4:
   st.markdown("<h3 style='text-align: center; color: white;'>Something Extra</h3>", unsafe_allow_html=True)
   st.image("./src/img/spotify_logo.png")

# ---*--- Streamlit WebApp Footer ---*---

st.markdown("---")
st.write(
    "Share on social media with the hashtag [#ccbda2023spotipyNX](https://twitter.com/) !"
)


# ---*---  ---*---
