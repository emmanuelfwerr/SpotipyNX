import pandas as pd
import numpy as np


def fetch_liked_tracks_DF(spotify: object, n: int) -> pd.DataFrame():
    """
    Fetch a user's saved songs using the spotify client.

    Args:
        spotify: A Spotipy object used to interact with the Spotify API

    Returns:
        liked_tracks_DF: A Pandas DataFrame with tracks and their metadata
    """
    liked_tracks_results = spotify.current_user_saved_tracks()
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

        audio_features = spotify.audio_features([track_uri])[0] #function requires a list

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
        main_artist = spotify.artist(main_artist_uri)
        liked_songs_df.loc[track_uri, "main_artist_name"] = main_artist["name"]
        liked_songs_df.loc[track_uri, "main_artist_followers"] = main_artist["followers"]["total"]
        liked_songs_df.loc[track_uri, "main_artist_genres"] = main_artist["genres"]
        liked_songs_df.loc[track_uri, "main_artist_popularity"] = main_artist["popularity"]

    return liked_songs_df


def fetch_top_tracks_DF(spotify: object, n: int) -> pd.DataFrame():
    """
    Fetch a user's top songs using the spotify client.

    Args:
        spotify: A Spotipy object used to interact with the Spotify API

    Returns:
        top_tracks_DF: A Pandas DataFrame with tracks and their metadata
    """
    top_tracks_results = spotify.current_user_top_tracks()
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

        audio_features = spotify.audio_features([track_uri])[0] #function requires a list

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
        main_artist = spotify.artist(main_artist_uri)
        top_songs_df.loc[track_uri, "main_artist_name"] = main_artist["name"]
        top_songs_df.loc[track_uri, "main_artist_followers"] = main_artist["followers"]["total"]
        top_songs_df.loc[track_uri, "main_artist_genres"] = main_artist["genres"]
        top_songs_df.loc[track_uri, "main_artist_popularity"] = main_artist["popularity"]

    return top_songs_df


def fetch_top_artists_DF(spotify: object, n: int) -> pd.DataFrame():
    """
    Fetch a user's top artists using the spotify client.

    Args:
        spotify: A Spotipy object used to interact with the Spotify API

    Returns:
        top_artists_DF: A Pandas DataFrame with artists and their metadata
    """
    top_artists_results = spotify.current_user_top_artists()
    top_artists = top_artists_results['items']

    # ---*--- Top Artists ^ ---*---

    

    return ...


def print_sample_output():

    return ...