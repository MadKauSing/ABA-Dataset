import pandas
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import csv
import os
import subprocess
import asyncio

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
  "4c0FH7ppMiVUJ8DB5zbfZg",
  "05l0uxjVm9sYLhxNWqWiWq",
  "4fmqHWih1dWw6qUqAKPwDY"
 ],
 "hindustani_classical": [
  "37i9dQZF1DX6EUcyVKIE73",
  "07TTxAhPmKr4Pw3A8GWcnv",
  "37i9dQZF1DX6QsiGlwQqfw",
  "5EZGFeeUWwY97K5evwdnOg",
  "66Szike9gNgaPYGmgOzmNF"
 ],
 "punjabi_hip_hop": [
  "37i9dQZF1DX5cZuAHLNjGz",
  "37i9dQZF1DWTqYqGLu7kTX",
  "37i9dQZF1DWXVJK4aT7pmk",
  "37i9dQZF1DXcQNdt1GHNdg",
  "37i9dQZF1DWStljCmevj7t"
  
 ],
 "ghazal": [
  "37i9dQZF1DXdsiL9gD4vAA",
  "37i9dQZF1EIdwYKvOYWK17",
  "3aVvXfZZds4cjdZXloUzuv",
  "0wXVTIXshvx7iQ3Az9zbR3",
  "4hgplT6M3ZsQqPfZyLTdAd",
 ],
 "desi_pop": [
  "5T5xOFP3qd3tZweafzeCsr",
  "37i9dQZF1DWTwzVdyRpXm1",
  "37i9dQZF1DX2RahGIyQXcJ",
  "6K6VUmYXzXNEutP6TlY4Kp",
  "3t1vRcdSF2zY5AAg2M4Vhz"
 ],
 "indian_indie": [
  "37i9dQZF1DX5q67ZpWyRrZ",
  "37i9dQZF1DX9Kz7jBbxgYQ",
  "37i9dQZF1DWXSzFkaLsPkN",
  "2cdkBS6JAmaKETJgS6npOU",
  "1VVZ572KDWdVQ0evr47Ybo"
 ],
 "sufi": [
  "0b9EKgAmUBaiBdZBrEhmnf",
  "37i9dQZF1DX2Y6ZOyTJZfp",
  "37i9dQZF1DX9mwNrgNa73l",
  "0pyaB6bcOQkq8D9J2hA5sy",
  "0ljyXS4LWIdQwqvhPsOTVC"
 ],
 "classic_bollywood": [
  "45kAbfAdCqx3DjnoByW5hg",
  "3krQQMaFu02sVvEqkiM2Do",
  "5pnKGZHKkbKiF1zyek0iyo",
  "055kvG2XzWqLe7fsMf6xmN",
  "37i9dQZF1EIggh88cylQBM"
 ],
 "tamil_pop": [
  "37i9dQZF1DX1i3hvzHpcQV",
  "37i9dQZF1DXaVmfUr97Uve",
  "08Esqeob5IXwMnqyavhXfJ",
  "09SURS86nZO6aKlMLOKgOL",
  "37i9dQZF1DX7vl8XKmpwdM"
 ],
 "bhojpuri_pop": [
  "6SBMhQ89bOrjB6BDI60Jrm",
  "37i9dQZF1DXayxAYAg0lzu",
  "4IzeGV3KMIxi7WMPqGaxDq",
  "5po4316Ru2In7DigYjg0bw",
  "06LiEciv9YZ4XLGqX5Vm4S"
 ]
}
#genre dict created
print(genre_dict)

os.system("rm -r aba")

# creating filesystem
os.system('mkdir aba')
for i in genres:
    os.system(f"mkdir aba\{i}")

fow=open("dataset.txt","w")

dataset=[]

song_limit=100

async def generator():
    for genre in genres:
        song_count=0

        #iterating through each playlist
        for playlist in genre_dict[genre]:
            res = spotify.playlist_items(playlist_id=playlist)

            #for each track
            for track in res['items']:
                id=track['track']['id']
                name=track['track']['name']
                genre=genre

                var=os.system(f"cd aba/{genre} && spotdl https://open.spotify.com/track/{id} --output-format mp3" )
                await asyncio.sleep(1)
                # os.wait()
                song_count=os.system(f"cd aba/{genre} && ls *.mp3 |wc -l")
                # os.wait()
                if var==0:
                    dataset.append([id,name,genre])
                if song_count>=song_limit:
                    break
                print(song_count,file=fow)
                print(song_count,file=fow)
            if song_count>=song_limit:
                break
        print(dataset,file=fow)
        

asyncio.run(generator())

