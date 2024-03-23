from dotenv import load_dotenv
load_dotenv()
import os

import spotipy
from spotipy import SpotifyClientCredentials

import pandas as pd
import matplotlib.pyplot as plt

#Connection
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
sp=spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id, client_secret))

#artist_uri = 'spotify:artist:503mwh1GWEiWy9bzzpiTFW'
results = sp.artist_top_tracks("503mwh1GWEiWy9bzzpiTFW")
tracks=results['tracks']
#print(tracks)

#Getting the name, popularity and duration (conversion included)
filtered_tracks=[]     
for track in tracks:
    filtered_track = {}
    for k, v in track.items():
        if k in ["duration_ms"]:
            filtered_track[k] = (v / (1000*60)) %60
        elif k in ["name", "popularity"]:
            filtered_track[k] = v
        else:
            continue
    filtered_tracks.append(filtered_track)
#print(filtered_tracks)

#Converting the results into a dataframe
af_tracks=pd.DataFrame.from_dict(filtered_tracks)

#Sorting the tracks to get the top 3
af_tracks.sort_values(by=['popularity'], ascending=False).head(3)

#Plotting to look for a possible correlation between the duration of the song and its popularity
plt.scatter(af_tracks['popularity'], af_tracks['duration_ms'], )
plt.xlabel("Song popularity")
plt.ylabel("Song duration in min")
plt.show()

#As shown, there is no correlation between the duration of the song and its popularity.