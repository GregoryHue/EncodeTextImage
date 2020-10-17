import time

from pathlib import Path


def Success(path):
    return print("Process is done. Check it here : ", path)


def ValueTooHIgh(value):
    return print("Value too high : " + value + " | " + chr(value))


def CheckingFile(path):
    return print('Checking if file : \"' + path + '\" exists . . .')


def CheckingType(type, bool):
    return print(bool, 'File type : ' + type)

def EndOfFile(type):
    return print("End of file " + type)

def FileFound(path):
    return print('File found here : ' + path)


def Error(typeError):
    message = ''
    message += 'There bas been an error : '
    if typeError == 1:
        message += 'File not found'
    elif typeError == 2:
        message += 'File wrong type'
    elif typeError == 3:
        message += ''
    elif typeError == 4:
        message += ''
    else:
        message += 'error unknown'

    return print(message)
