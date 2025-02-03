import os
from colorama import Style,Fore

class Config:
    def __init__(self):
        self.pytubefix = Pytubefix()
    def clear(self):
        if os.name == 'nt': 
            os.system('cls')
        else:  
            os.system('clear')


class Pytubefix:
    def __init__(self):
        self.innertube = Innertube(self)

    def access_to_pytubefix(self):
        lib_dir = "./lib"
        try:
            dir_array = os.listdir(lib_dir)
            if not dir_array:
                raise FileNotFoundError("No se encontraron subdirectorios en './lib'.")
            pytubefix_path = f"{lib_dir}/{dir_array[0]}/site-packages/pytubefix"
            if not os.path.exists(pytubefix_path):
                raise FileNotFoundError(f"No se encontró la ruta: {pytubefix_path}")
            return pytubefix_path
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return None

class Innertube:
    def __init__(self, pytubefix):
        self.pytubefix = pytubefix
        pytubefix_path = self.pytubefix.access_to_pytubefix()
        if pytubefix_path:
            self.path = f"{pytubefix_path}/innertube.py"
        else:
            self.path = None

    def replace_token_verifier(self):
        if not self.path or not os.path.exists(self.path):
            print(f"No se puede abrir el archivo porque la ruta '{self.path}' no es válida.")
            return

        try:
            with open(self.path, "r") as file:
                data = file.readlines()
                index= 528
                for i in range(2):
                    lineInput = data[index+i].split("=")
                    lineInput[1]=' "" \n' 
                    data[index+i] = '='.join(lineInput)

            with open(self.path, "w") as file:
                file.writelines(data)
                print(f"{Fore.GREEN}Configure Succes!{Fore.WHITE}")

        except Exception as e:
            print(f"{Fore.RED}Error to read the file Innertube.py: {Fore.WHITE}{e}")

