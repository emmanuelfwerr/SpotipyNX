import streamlit as st
from src.ui import *

# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
#st.image("src/img/home_banner.png")
add_logo()
sidebar()

st.header("📨 Help Us Improve With Your Feedback!")
st.write("We will get back to you personally as soon as we fix your bug or add the feature you have requested")

contact_form = """
<form action="https://formsubmit.co/spotipy.nx@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---*--- Streamlit WebApp Footer ---*---
st.markdown("---")
st.write(
    "Share on social media with the hashtag [#ccbda2023spotipyNX](https://twitter.com/) !"
)
    