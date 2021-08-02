

def Success(path):
    return print("Process is done. Check it here : ", path)


def ValueTooHIgh(value):
    return print("Value too high : " + value + " | " + chr(value))


def CheckingFile(path):
    return print('Checking if file : \"' + path + '\" exists . . .')


def CheckingType(type):
    return print('File type : ' + type)


def EndOfFile(type):
    return print("End of file " + type)


def FileFound(path):
    return print('File found here : ' + path)


def Error(type_error):
    message = ''
    message += 'There bas been an error : '
    if type_error == 1:
        message += 'File not found'
    elif type_error == 2:
        message += 'File wrong type'
    elif type_error == 3:
        message += ''
    elif type_error == 4:
        message += ''
    else:
        message += 'error unknown'

    return print(message)
