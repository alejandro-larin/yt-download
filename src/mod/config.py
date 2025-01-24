import os

class Config:
    def __init__(self):
        self.pytubefix=Pytubefix()


class Pytubefix:
    def __init__(self):
        def AccesToPutubefix(self):
            dir= "./lib"
            dirArray=os.listdir(dir)
            dir=f"./lib/{dirArray[0]}/site-packages/pytubefix"
            return dir
            

class Innertube(Pytubefix):
    def __init__(self):
        path=f"{self.AccesToPutubefix()}/innertube.py"
        def replacePoTokendVerifier(self):
            with open(path, "r+") as file:
                data = file.read()


