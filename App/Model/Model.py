import App.View.View as View

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
        View.CheckingType(file)
        return True
    else:
        View.Error(2)
        View.CheckingType(file)
        return False


def FileIsPng(path):
    file = Path(path)
    if file.suffix == '.png':
        View.CheckingType(file.suffix)
        return True
    else:
        View.Error(2)
        View.CheckingType(file.suffix)
        return False


def FindFile(path):
    View.CheckingFile(path)

    file = Path(path)
    if file.is_file():
        abso_path = str(file.resolve())
        View.FileFound(abso_path)
        return True
    else:
        View.Error(1)
        return False


def ImageOpened(path):
    return Image.open(path)
