

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from subprocess import Popen
from subprocess import PIPE
import subprocess

CLIENT_ID = "834e7549e0fb4b4a89ca4ba4ead45f93"
CLIENT_SECRET = "470a82dcfc844634ad6705a1a191866d"
REDIRECT= "http://localhost:8888/callback"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT, scope=scope))
spotify=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT))
files=open('./genres.txt','r')

genres=[x.strip('\n') for x in files.readlines()]
#genres

genres=['sufi']

genre_dict={

  "sufi": [
  "37i9dQZF1DX9mwNrgNa73l",
  "0pyaB6bcOQkq8D9J2hA5sy",
  "0ljyXS4LWIdQwqvhPsOTVC"
 ]
}
#genre dict created
print(genre_dict)

#os.system("rm -r aba")

# creating filesystem
os.system('mkdir aba')
for i in genres:
    os.system(f"mkdir aba/{i}")

fow=open("dataset.txt","w")

dataset=[]

song_limit=100
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
            

            #searching
            search=Popen(["spotdl",f"https://open.spotify.com/track/{id}","--output-format","mp3"],stdout=PIPE, stderr=PIPE, universal_newlines=True,cwd=f"aba/{genre}")
            search.wait()

            print("searching and downloading")
            #checking count
            c1 = Popen(("ls"), stdout=PIPE, stderr=PIPE, universal_newlines=True,cwd=f'aba/{genre}')
            c1.wait()
            print()
            c2 = Popen(["wc","-l"], stdin=c1.stdout, stdout=PIPE,cwd=f"aba/{genre}")
            c2.wait()
            print()
            output, errors = c2.communicate()
            song_count=int(str(output).replace("b","").replace("\\n","").replace("'",""))
            print(song_count)

    
            if song_count>=song_limit:
                break

        if song_count>=song_limit:
            break
    print(dataset,file=fow)
        



