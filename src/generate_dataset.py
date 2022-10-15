import pandas
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import csv

CLIENT_ID = "834e7549e0fb4b4a89ca4ba4ead45f93"
CLIENT_SECRET = "470a82dcfc844634ad6705a1a191866d"
REDIRECT= "http://localhost:8888/callback"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT, scope=scope))
spotify=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT))
files=open('./genres.txt','r')

genres=[x.strip('\n') for x in files.readlines()]
#genres

genre_dict={
 "carnatic": [
  "37i9dQZF1DX4tCh1BbG63z",
  "37i9dQZF1DXcQDIWVt93jl",
  "4c0FH7ppMiVUJ8DB5zbfZg"
 ],
 "hindustani classical": [
  "37i9dQZF1DX6EUcyVKIE73",
  "07TTxAhPmKr4Pw3A8GWcnv",
  "37i9dQZF1DX6QsiGlwQqfw"
 ],
 "punjabi hip hop": [
  "37i9dQZF1DX5cZuAHLNjGz",
  "37i9dQZF1DWTqYqGLu7kTX",
  "37i9dQZF1DWXVJK4aT7pmk"
 ],
 "ghazal": [
  "37i9dQZF1DXdsiL9gD4vAA",
  "37i9dQZF1EIdwYKvOYWK17",
  "3aVvXfZZds4cjdZXloUzuv"
 ],
 "desi pop": [
  "5T5xOFP3qd3tZweafzeCsr",
  "37i9dQZF1DWTwzVdyRpXm1"
 ],
 "indian indie": [
  "37i9dQZF1DX5q67ZpWyRrZ",
  "37i9dQZF1DX9Kz7jBbxgYQ",
  "37i9dQZF1DWXSzFkaLsPkN"
 ],
 "sufi": [
  "0b9EKgAmUBaiBdZBrEhmnf",
  "37i9dQZF1DX2Y6ZOyTJZfp",
  "37i9dQZF1DX9mwNrgNa73l"
 ],
 "classic bollywood": [
  "45kAbfAdCqx3DjnoByW5hg",
  "3krQQMaFu02sVvEqkiM2Do"
 ],
 "tamil pop": [
  "37i9dQZF1DX1i3hvzHpcQV",
  "37i9dQZF1DXaVmfUr97Uve",
  "08Esqeob5IXwMnqyavhXfJ"
 ],
 "bhojpuri pop": [
  "6SBMhQ89bOrjB6BDI60Jrm",
  "37i9dQZF1DXayxAYAg0lzu",
  "4IzeGV3KMIxi7WMPqGaxDq"
 ]
}

# genre_dict=json.dumps(genre_dict,indent=1)
print(genre_dict)

# # Going through playlists from each genre and adding songs to them
# dataset = []

# for genre,playlist in genre_dict.items():
#     res = spotify.playlist_items(playlist_id=playlist)
#     song_count = 0
#     if song_count % 100 == 0 and song_count != 0:
#             break
    
#     for track in res['items']:
#         artist_names = []
#         for artist_name in track['track']['album']['artists']:
#             artist_names.append(artist_name['name'])
#         data = [ track['track']['id'],track['track']['name'],artist_names,genre ]
#         if data in dataset:
#             continue
#         else:
#             dataset.append(data)
        
#         song_count += 1
#         if song_count % 100 == 0 and song_count != 0:
#             break

# headers = ['id','name','artists','genre']

# with open("../dataset.csv", 'w', encoding='UTF8',newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     writer.writerows(dataset)

dataset = []

for genre in genres:
    song_count = 0
    for playlist in genre_dict[genre]:
        try:
            res = spotify.playlist_items(playlist_id=playlist)
            if song_count % 100 == 0 and song_count != 0:
                    break
            for track in res['items']:
                artist_names = []
                for artist_name in track['track']['album']['artists']:
                    artist_names.append(artist_name['name'])
                
                data = [ track['track']['id'],track['track']['name'],artist_names,genre ]
                if data in dataset:
                    continue
                else:
                    dataset.append(data)
                
                song_count += 1
                if song_count % 100 == 0 and song_count != 0:
                    break
        except:
            print("Invalid playlist: ",playlist)

headers = ['id','name','artists','genre']

with open("../dataset.csv", 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(dataset)