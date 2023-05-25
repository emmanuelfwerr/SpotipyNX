import os
import streamlit.components.v1 as components
import streamlit as st
from dotenv import load_dotenv
from pyvis.network import Network
from src.ui import *
from src.s3 import *
import time
import string
import random


# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
add_logo()
sidebar()

if not "keep_graphics" in st.session_state:
    st.session_state.keep_graphics = False

generate_network = st.button('Build Your Music Network')

if generate_network:
    st.session_state.keep_graphics = True # este hack esta bastante chetao para que no refresque toda

if st.session_state.keep_graphics:
    try:
        top_tracks_results = st.session_state.spotify.current_user_top_tracks(
            limit=169, offset=0, time_range='medium_term'
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

        with st.form(key="form_email"):
            input_email_address = st.text_input('Email address:')
            input_email_name = st.text_input('Name (optional)')
            send_network_email = st.form_submit_button(
                'Send Your Music Network',
                #disabled=(input_email_address=="")
            )

    except Exception as e:
        print(e)

    if send_network_email and not input_email_address == "":
        try:
            file_name = "music_net.html"
            new_name = str(time.time()) + ''.join(random.choice(string.ascii_uppercase) for _ in range(6)) + "_"+file_name
            s3_url = uploadS3(file_name, new_name)
            sendEmail2(s3_url, input_email_address,
                       f"{input_email_name}, here is your music network!")

            st.text("Your music network has been sent!")

        except Exception as e:
            print(e)
            st.text("Sorry for the inconveniences, this functionality is currently not available")


# ---*--- Streamlit WebApp Footer ---*---
st.markdown("---")
st.write(
    "Share on social media with the hashtag [#ccbda2023spotipyNX](https://twitter.com/) !"
)