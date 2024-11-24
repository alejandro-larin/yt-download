from os import mkdir,path
def dir_create(path):
    isExist = path.exists(path) 

    if isExist:
        mkdir(path)
    else:
        print("Directory existing!")