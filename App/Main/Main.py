import math
from PIL import Image

import App.Model.Model as model
import App.Controller.Controller as controller
import App.View.View as view

import sys
from PIL import Image

path = 'Files/intxt.txt'


def main():
    if model.FindFile(path):
        controller.EncodeTxtToImg(path)
        if model.FindFile(model.GetFolderOfFile(path) + model.GetFileName(path) + "_Ncoded.png"):
            controller.DecodeImgToTxt(model.GetFolderOfFile(path) + model.GetFileName(path) + "_Ncoded.png")
    else:
        exit(0)


if __name__ == '__main__':
    main()


#TODO
# - Utiliser des valeur Unicode unitile pour marquer début et fin de fichier text