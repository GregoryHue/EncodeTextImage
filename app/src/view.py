class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Success(path):
    return print(bcolors.OKCYAN + "Process is done. Check it here: ", path + '\n' + bcolors.ENDC)

def TryingToEncode(path):
    return print(bcolors.OKCYAN + "Trying to encode." + bcolors.ENDC)

def TryingToDecode(path):
    return print(bcolors.OKCYAN + "Trying to decode." + bcolors.ENDC)

def ValueTooHIgh(value):
    return print(bcolors.OKCYAN + "Value too high: " + value + " | " + chr(value) + bcolors.ENDC)


def CheckingFile(path):
    return print(bcolors.OKCYAN + "\nSearching for: " + path + bcolors.ENDC)


def CheckingType(type):
    return print('File type: ' + type)


def EndOfFile(type):
    return print(bcolors.OKCYAN + "End of " + type + " file." + bcolors.ENDC)


def FileFound(path):
    return print(bcolors.OKCYAN + 'File found here: ' + path + bcolors.ENDC)


def Error(type_error):
    message = ''
    message += bcolors.FAIL + 'There bas been an error : '
    if type_error == 1:
        message += 'File not found'
    elif type_error == 2:
        message += 'File wrong type'
    elif type_error == 3:
        message += '' + bcolors.ENDC
    elif type_error == 4:
        message += '' + bcolors.ENDC
    else:
        message += 'error unknown'

    message += '\n' + bcolors.ENDC

    return print(message)
