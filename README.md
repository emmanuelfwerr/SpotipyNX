# SpotipyNX
## Basic Demo WebApp

It is easy to set up simple data driven web applications to interact with your data, even using lighter frameworks than django or flask. For this simple demo we will explore [Streamlit](https://streamlit.io). Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. 

The code used to run the following demo is in the `1_🏠_Home.py.py` script in the root directory of this repo.

The first step is to create a virtual environment with the necessary packages, listed in the `requirements.txt` file. After this is done, make sure to create a .env file in the root directory of your project where you set your Spotify App Credentials. It should look like this:

```env
SPOTIPY_CLIENT_ID='<Your Spotify Client ID>'
SPOTIPY_CLIENT_SECRET='<Your Spotify Client ID>'
SPOTIPY_REDIRECT_URI='<The exact Redirect URI you set in your Spotify App>'
```

The next step is to clone this repo, open your terminal in the root directory, and run the following statement:

```bash
streamlit run 1_🏠_Home.py
```

This will trigger Streamlit to begin running your application script and will redirect you to your site in a localhost port, where you will encounter the demo app and a few buttons. Click on the button that says "Spotify OAuth", which will take you to Spotify's portal so you can securely connect to your account and grant "your app" permission to view your account data. After this is done, streamlit will bring you back to your homepage and display some of the most recent songs you have downloaded in your liked songs, along with a little surprise.

If you want to learn more about the different parts of the code, open up the `demo.py` script and go through it. It is quite simple to build out this functionality in a single python script using Streamlit. It is definitely not as robust as Django or even Flask, but it is quite capable for simpler data-centric webapps.
