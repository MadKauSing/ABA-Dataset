from subprocess import Popen
import subprocess
print("check")
def download(id,genre):
    search=Popen(["spotdl",f"https://open.spotify.com/track/{id}","--output-format","mp3"],stdout=PIPE, stderr=PIPE, universal_newlines=True,cwd=f"aba/{genre}")
    search.wait()
            







search=Popen(["spotdl", "\"The Anirudh Varma Collective, Sowmya Gurucharan, Abhay Nayampally, Varun Rajasekharan, Madhur Chaudhary - Vasanthi (Live)\" --output-format mp3"],cwd="aba/carnatic")
#search=Popen(["cd aba/carnatic && spotdl \"The Anirudh Varma Collective, Sowmya Gurucharan, Abhay Nayampally, Varun Rajasekharan, Madhur Chaudhary - Vasanthi (Live)\" --output-format mp3"] )
search.wait()
print("done",search)