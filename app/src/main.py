import controller
import model

path = 'app/files/intxt.txt'

def main():
    if model.FindFile(path):
        controller.EncodeTxtToImg(path)
        if model.FindFile(model.GetFolderOfFile(path) + model.GetFileName(path) + "_Ncoded.png"):
            controller.DecodeImgToTxt(model.GetFolderOfFile(path) + model.GetFileName(path) + "_Ncoded.png")
    else:
        exit(0)


if __name__ == '__main__':
    main()

# TODO
# - Compare original text file and generated text file
