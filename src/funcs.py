import pandas as pd
import numpy as np
import streamlit as st


# ---*--- Enable DataFrame Downloads ---*---
@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


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
            "danceability", "energy", "key",
            "loudness", "mode", "speechiness",
            "acousticness", "instrumentalness",
            "liveness", "valence", "tempo", "type",
            "duration", "time_signature", "main_artist_uri",
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

        liked_songs_df.loc[track_uri, "danceability"] = audio_features["danceability"]
        liked_songs_df.loc[track_uri, "energy"] = audio_features["energy"]
        liked_songs_df.loc[track_uri, "key"] = audio_features["key"]
        liked_songs_df.loc[track_uri, "loudness"] = audio_features["loudness"]
        liked_songs_df.loc[track_uri, "mode"] = audio_features["mode"]
        liked_songs_df.loc[track_uri, "speechiness"] = audio_features["speechiness"]
        liked_songs_df.loc[track_uri, "acousticness"] = audio_features["acousticness"]
        liked_songs_df.loc[track_uri, "instrumentalness"] = audio_features["instrumentalness"]
        liked_songs_df.loc[track_uri, "liveness"] = audio_features["liveness"]
        liked_songs_df.loc[track_uri, "valence"] = audio_features["valence"]
        liked_songs_df.loc[track_uri, "tempo"] = audio_features["tempo"]
        liked_songs_df.loc[track_uri, "type"] = audio_features["type"]
        liked_songs_df.loc[track_uri, "duration"] = audio_features["duration_ms"]
        liked_songs_df.loc[track_uri, "time_signature"] = audio_features["time_signature"]

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
            "danceability", "energy", "key",
            "loudness", "mode", "speechiness",
            "acousticness", "instrumentalness",
            "liveness", "valence", "tempo", "type",
            "duration", "time_signature", "main_artist_uri",
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

        top_songs_df.loc[track_uri, "danceability"] = audio_features["danceability"]
        top_songs_df.loc[track_uri, "energy"] = audio_features["energy"]
        top_songs_df.loc[track_uri, "key"] = audio_features["key"]
        top_songs_df.loc[track_uri, "loudness"] = audio_features["loudness"]
        top_songs_df.loc[track_uri, "mode"] = audio_features["mode"]
        top_songs_df.loc[track_uri, "speechiness"] = audio_features["speechiness"]
        top_songs_df.loc[track_uri, "acousticness"] = audio_features["acousticness"]
        top_songs_df.loc[track_uri, "instrumentalness"] = audio_features["instrumentalness"]
        top_songs_df.loc[track_uri, "liveness"] = audio_features["liveness"]
        top_songs_df.loc[track_uri, "valence"] = audio_features["valence"]
        top_songs_df.loc[track_uri, "tempo"] = audio_features["tempo"]
        top_songs_df.loc[track_uri, "type"] = audio_features["type"]
        top_songs_df.loc[track_uri, "duration"] = audio_features["duration_ms"]
        top_songs_df.loc[track_uri, "time_signature"] = audio_features["time_signature"]

        main_artist_uri = track["artists"][0]["uri"]
        top_songs_df.loc[track_uri, "main_artist_uri"] = main_artist_uri
        main_artist = st.session_state.spotify.artist(main_artist_uri)
        top_songs_df.loc[track_uri, "main_artist_name"] = main_artist["name"]
        top_songs_df.loc[track_uri, "main_artist_followers"] = main_artist["followers"]["total"]
        top_songs_df.loc[track_uri, "main_artist_genres"] = main_artist["genres"]
        top_songs_df.loc[track_uri, "main_artist_popularity"] = main_artist["popularity"]

    return top_songs_df