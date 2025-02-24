def downloadVideo():
    print("descargando video")


def downloadVideo():
    print("descargando video")


options = [
    ["Playlist", "Video"],
    ["Mp3", "Mp4"]
]


def showMenu(array):
    for index, option in enumerate(array, start=1):
        print(f"{index}. {option}")


def choicedOption(select, array):
    if 1 <= select <= len(array): 
        option= array[select-1]
        print(f"Has seleccionado: {option}")
        # sleep(2)
        # config.clear()
        # downloadPlaylist
        
        print('Descargando Playlist')
        print("Desacargando Video")
        
    else:
        print("Selección no válida")


def menu():
    print("Seleccione una opción:")
    showMenu(options[0])
    select = int(input("Ingrese el número de la opción: ")) 
    choicedOption(select, options[0])  


menu()
