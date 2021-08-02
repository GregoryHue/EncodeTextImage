import App.Controller.Controller as Controller
import App.Model.Model as Model

import sys


path = 'Files/intxt.txt'

def main():
    if Model.FindFile(path):
        Controller.EncodeTxtToImg(path)
        if Model.FindFile(Model.GetFolderOfFile(path) + Model.GetFileName(path) + "_Ncoded.png"):
            Controller.DecodeImgToTxt(Model.GetFolderOfFile(path) + Model.GetFileName(path) + "_Ncoded.png")
    else:
        exit(0)


if __name__ == '__main__':
    main()

# TODO
# - Utiliser des valeur Unicode inutile pour marquer début et fin de fichier text
