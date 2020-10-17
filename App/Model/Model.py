import App.View.View as view

from PIL import Image
from pathlib import Path


class Color:
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha


def GetFileName(path):
    return Path(path).stem


def GetFolderOfFile(path):
    return str(Path(path).parent) + "\\"


def GetAbsoFolderOfFile(path):
    return str(Path(path).resolve())


def FileIsTxt(path):
    file = Path(path)
    if file.suffix == '.txt':
        view.CheckingType(file)
        return True
    else:
        view.Error(2)
        view.CheckingType(file)
        return False


def FileIsPng(path):
    file = Path(path)
    if file.suffix == '.png':
        view.CheckingType(file.suffix, True)
        return True
    else:
        view.Error(2)
        view.CheckingType(file.suffix, False)
        return False


def FindFile(path):
    view.CheckingFile(path)

    file = Path(path)
    if file.is_file():
        abso_path = str(file.resolve())
        view.FileFound(abso_path)
        return True
    else:
        view.Error(1)
        return False


def ImageOpened(path):
    return Image.open(path)
