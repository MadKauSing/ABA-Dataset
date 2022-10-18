import pandas
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import csv
import os

CLIENT_ID = "834e7549e0fb4b4a89ca4ba4ead45f93"
CLIENT_SECRET = "470a82dcfc844634ad6705a1a191866d"
REDIRECT= "http://localhost:8888/callback"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT, scope=scope))
spotify=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT))
files=open('./genres.txt','r')

genres=[x.strip('\n') for x in files.readlines()]
#genres

genres=[x.replace(' ','_') for x in genres]

genre_dict={
 "carnatic": [
  "37i9dQZF1DX4tCh1BbG63z",
  "37i9dQZF1DXcQDIWVt93jl",
  "4c0FH7ppMiVUJ8DB5zbfZg"
 ],
 "hindustani_classical": [
  "37i9dQZF1DX6EUcyVKIE73",
  "07TTxAhPmKr4Pw3A8GWcnv",
  "37i9dQZF1DX6QsiGlwQqfw"
 ],
 "punjabi_hip_hop": [
  "37i9dQZF1DX5cZuAHLNjGz",
  "37i9dQZF1DWTqYqGLu7kTX",
  "37i9dQZF1DWXVJK4aT7pmk"
 ],
 "ghazal": [
  "37i9dQZF1DXdsiL9gD4vAA",
  "37i9dQZF1EIdwYKvOYWK17",
  "3aVvXfZZds4cjdZXloUzuv"
 ],
 "desi_pop": [
  "5T5xOFP3qd3tZweafzeCsr",
  "37i9dQZF1DWTwzVdyRpXm1"
 ],
 "indian_indie": [
  "37i9dQZF1DX5q67ZpWyRrZ",
  "37i9dQZF1DX9Kz7jBbxgYQ",
  "37i9dQZF1DWXSzFkaLsPkN"
 ],
 "sufi": [
  "0b9EKgAmUBaiBdZBrEhmnf",
  "37i9dQZF1DX2Y6ZOyTJZfp",
  "37i9dQZF1DX9mwNrgNa73l"
 ],
 "classic_bollywood": [
  "45kAbfAdCqx3DjnoByW5hg",
  "3krQQMaFu02sVvEqkiM2Do"
 ],
 "tamil_pop": [
  "37i9dQZF1DX1i3hvzHpcQV",
  "37i9dQZF1DXaVmfUr97Uve",
  "08Esqeob5IXwMnqyavhXfJ"
 ],
 "bhojpuri_pop": [
  "6SBMhQ89bOrjB6BDI60Jrm",
  "37i9dQZF1DXayxAYAg0lzu",
  "4IzeGV3KMIxi7WMPqGaxDq"
 ]
}
print(genre_dict)

# Reset the filesystem
os.system("rm -r aba")

#creating filesystem
os.system('mkdir aba')
for i in genres:
    os.system(f"mkdir aba/{i}")


dataset = []
song_limit_per_genre = 100

for genre in genres:
    song_count = 0
    for playlist in genre_dict[genre]:
        try:
            genre=genre.replace(' ','_')
            res = spotify.playlist_items(playlist_id=playlist)
            if song_count % song_limit_per_genre == 0 and song_count != 0:
                    break
            for track in res['items']:
                artist_names = []
                for artist_name in track['track']['album']['artists']:
                    artist_names.append(artist_name['name'])
                
                data = [ track['track']['id'],track['track']['name'],artist_names,genre ]
                var=os.system(f"cd aba/{genre} && spotdl https://open.spotify.com/track/{data[0]} --output-format mp3" )
                #download the song also
                if var!=0 or data in dataset or track['track']['name'] == '':
                    print(data)
                    continue
                else:
                    dataset.append(data)
                    song_count += 1
                
                if song_count % song_limit_per_genre == 0 and song_count != 0:
                    break
        except:
            print("Invalid playlist: ",playlist)

headers = ['id','name','artists','genre']

with open("dataset.csv", 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(dataset)