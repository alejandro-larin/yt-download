import os
from time import sleep
from colorama import Style,Fore

class Config:
    def __init__(self):
        self.pytubefix = Pytubefix(self)

    def clear(self):
        if os.name == 'nt': 
            os.system('cls')
        else:  
            os.system('clear')

    def create_output(self, path):
        isExist = os.path.exists(path) 

        if not isExist:
            try:
                os.mkdir(path)
                print(f"{Fore.YELLOW}✅ Directory {path} created")
                sleep(1.0)
                self.clear()
            except OSError:
                print(f"{Fore.RED}❌ Creation of the directory {path} failed")
                sleep(1.0)
                self.clear()
        else:
            print(f"{Fore.GREEN}✅ Directory is ready!")
            sleep(1.0)
            self.clear()

class Pytubefix:
    def __init__(self, config):
        self.config = config
        self.innertube = Innertube(self, config)

    def access_to_pytubefix(self):
        lib_dir = "./lib"
        try:
            dir_array = os.listdir(lib_dir)
            if not dir_array:
                raise FileNotFoundError(f"{Fore.RED}❌ Not foud  subdirectorys en './lib'.")
            pytubefix_path = f"{lib_dir}/{dir_array[0]}/site-packages/pytubefix"
            if not os.path.exists(pytubefix_path):
                raise FileNotFoundError(f"{Fore.RED}❌ Not foud route: {pytubefix_path}")
            return pytubefix_path
        except FileNotFoundError as e:
            print(f"{Fore.RED}❌ Error: {e}")
            return None

class Innertube:
    def __init__(self, pytubefix, config):
        self.config = config
        self.pytubefix = pytubefix
        pytubefix_path = self.pytubefix.access_to_pytubefix()
        if pytubefix_path:
            self.path = f"{pytubefix_path}/innertube.py"
        else:
            self.path = None
        

    def replace_token_verifier(self):
        try:
            with open(self.path, "r") as file:
                data = file.readlines()
                index= 528
                data[index-1]="\n"
                for i in range(2):
                    lineInput = data[index+i].split("=")
                    lineInput[1]=' "" \n' 
                    data[index+i] = '='.join(lineInput)
            with open(self.path, "w") as file:
                file.writelines(data)
                print(f"{Fore.GREEN}✅ Configure Succes!")
                sleep(1.0)
        except Exception as e:
            print(f"{Fore.RED}❌ Error to read the file Innertube.py: {Fore.WHITE}{e}")
            sleep(1.0)
