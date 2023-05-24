import os
import streamlit.components.v1 as components
import streamlit as st
from dotenv import load_dotenv
from pyvis.network import Network
from src.ui import *


# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
add_logo()
sidebar()

network_start = st.button('press me')

if network_start:
    try:
        top_tracks_results = st.session_state.spotify.current_user_top_tracks(
            limit=50, offset=0, time_range='medium_term'
        )

        tracks = []
        for top_track in top_tracks_results['items']:
            track = {
                "id": top_track.get("id"),
                "name": top_track.get("name"),
                "popularity": top_track.get("popularity")
            }

            album = top_track.get("album")
            track["album"] = {
                "id":album.get("id"),
                "name":album.get("name"),
                "release_date":album.get("release_date"),
                "artists":[
                {"id": artist.get("id"), "name": artist.get("name")} for artist in album.get("artists")
                ]
            }

            artists = top_track.get("artists")
            track["artists"] = [
                {"id": artist.get("id"), "name": artist.get("name")} for artist in artists
                ]

            tracks.append(track)

        try:
            os.remove(".cache")
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)


    try:
        net = Network(height="1000px", width="1600px", font_color="black")
        net.barnes_hut()
        for track in tracks:
            track_id = track.get("id")
            track_name = track.get("name")
            net.add_node(track_id, label=track_name, group="track", color="#FFC300",
                         title="Track - " + track_name)

            album = track.get("album")
            album_id = album.get("id")
            album_name = album.get("name")
            net.add_node(album_id, label=album_name, group="album", color="#FF5733",
                         title="Album - " + album_name, value=400)
            net.add_edge(track_id, album_id)
            artists = track.get("artists")
            for artist in artists:
                artist_id = artist.get("id")
                artist_name = artist.get("name")
                net.add_node(artist_id, label=artist_name, group="artist", color="#DAF7A6",
                             title="Artist - " + artist_name)
                net.add_edge(album_id, artist_id)

        net.show("music_net.html")
        net.show_buttons(filter_=['physics'])

        HtmlFile = open("music_net.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        components.html(source_code, height=1000, width=1600)

    except Exception as e:
        print(e)


# ---*--- Streamlit WebApp Footer ---*---

st.markdown("---")
st.write(
    "Share on social media with the hashtag [#ccbda2023spotify](https://twitter.com/) !"
)
