import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import altair as alt
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from src.ui import *

# ---*--- Streamlit WebApp Header ---*---
st.set_page_config(
    page_title="Spotify WebApp Mini Demo", page_icon="💥", layout="wide"
)
sidebar()

st.markdown('# Daily Top 10 - Spain')

# Row A
st.markdown('## Most popular songs')
lz_uri = '37i9dQZEVXbNFJfN1Vw8d9'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.playlist_items(lz_uri,fields='items,uri,name,id,total', market='us')

liked_songs_df = pd.DataFrame(
        columns=[
            "track_name", 
            "track_artists", "url_song"
        ])
for idx,track in enumerate(results['items'][:10]):
    artists = [art['name'] for art in track['track']['artists']]
    
    liked_songs_df.loc[idx, "track_name"] = track['track']['name']
    liked_songs_df.loc[idx, "track_artists"] = ', '.join(artists)
    liked_songs_df.loc[idx,"url_song"] = track['track']['preview_url']

for idx in liked_songs_df.index:
    with st.container():
        col0, col1, col2, col3  = st.columns([1,3,3,3])
        col0.write(idx + 1)
        col1.write(liked_songs_df['track_name'][idx]) 
        col2.write(liked_songs_df['track_artists'][idx])
        with col3:
            st.audio(liked_songs_df['url_song'][idx], format="audio/mp3")                            

# Row B 
palette = sns.color_palette("Greens_d", 10)
col1, col2 = st.columns(2)

# Col 1
with col1:
    st.markdown('### Streamings')  
    dfs = pd.read_html('https://kworb.net/spotify/country/es_daily.html')
    df_streamings = dfs[0][['Artist and Title','Streams']].head(10)
    df_streamings['Artist and Title'] = df_streamings['Artist and Title'].apply(lambda x: (x.split(' - ')[1]).split(" (")[0])
    
    fig1 = plt.subplots(1)
    plot1 = sns.barplot(x='Streams',y="Artist and Title", data=df_streamings, palette=palette)
    plot1.set_ylabel('')
    plot1.tick_params( colors='green')
    fig1 = plot1.get_figure()
    st.pyplot(fig1, transparent = True)

#  Col2
with col2:
    st.markdown('### Genres')    
    list = []
    for idx,track in enumerate(results['items'][:10]):
        for artist in track['track']['artists']:
            genres = spotify.artist(artist['uri'])['genres']
            list.extend(genres)
            
# OPTION 1
# fig, ax = plt.subplots()
# ax.hist(list, bins=20, orientation="horizontal")
# st.pyplot(fig)

# OPTION 2
# map = Counter(list)
# df_g = pd.DataFrame(
#         columns=[
#             "Genres", 
#             "Counter"
#         ])
# idx = 0
# for key, value in map.items():
#     df_g.loc[idx,"Genres"] = key
#     df_g.loc[idx,"Counter"] = value
#     idx = idx + 1

# st.bar_chart( pd.DataFrame.listfrom_dict(map,orient='index',columns=['Count']))
# fig, ax = plt.subplots()
# ax.hist(df_g, bins=20, orientation="horizontal")
# st.pyplot(fig)


    source = pd.DataFrame(
        {'genres': list}
    )
# OPTION 3

# st.write(alt.Chart(source).transform_aggregate(
#     count='count()',
#     groupby=['genres']
# ).transform_window(
#     rank='rank(count)',
#     sort=[alt.SortField('count', order='descending')]
# ).transform_filter(
#     alt.datum.rank < 10
# ).mark_bar().encode(
#     y=alt.Y('genres:N', sort='-x'),
#     x='count:Q',
# ))

# OPTION 4
    fig = plt.subplots(1)
    plot = sns.countplot(y='genres',data=source,order=source['genres'].value_counts().index[:10], palette=palette)
    plot.tick_params( colors='green')
    fig = plot.get_figure()
    st.pyplot(fig, transparent = True)


