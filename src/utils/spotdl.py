import os
class SpotDL_Downloader():
    def __init__(self,path):
        self.path=path
    def download(self,uid):    
        path=self.path
        os.system(f'cd {path}')        
        os.system(f'spotdl download https://open.spotify.com/track/{uid}')
    

        