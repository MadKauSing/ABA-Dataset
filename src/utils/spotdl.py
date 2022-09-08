import os
class SpotDL_Downloader():
    def __init__(self,genre):
        self.genre=genre
    def download(self,uid):    
        path=self.path
        os.system(f'cd /abad/{genre}')        
        os.system(f'spotdl download https://open.spotify.com/track/{uid}')
        os.system('cd ..')
        os.system('cd ..')
        
