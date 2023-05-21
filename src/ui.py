import base64
import streamlit as st
from PIL import Image

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
    with st.sidebar:
        image = Image.open('src/img/spotify.gif')
        st.markdown(
            "## How to use\n"
            "1. Connect Spotify Account using the `Spotify OAuth` button\n"
            "2. Browse the app while we process your data\n"
            "3. Enjoy 🤗\n"
        )

        st.markdown("---")
        st.markdown(
            "## How this works\n"
            "This app was built with [Streamlit](https://streamlit.io) using the"
            " [Spotify Web API](https://developer.spotify.com/documentation/web-api) and ... "
        )
        st.markdown("---")
        st.markdown("**Take results with a grain of** 🧂\n\n"
            "There's a lot that can be improved to make this app better.\n\n"
            "For more on how this was built, instructions to run locally and to contribute: [visit GitHub](https://github.com/)"
        )
        st.markdown("---")


def add_logo():
    '''@st.cache_data
    def get_image_as_base_64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    img = get_image_as_base_64('./src/img/spotify_logo.png')'''

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