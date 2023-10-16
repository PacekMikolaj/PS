import sys


def checkIfParamIsUsed(param, params):
    try:
        if params.index(param) != ValueError:
            return params.index(param)
    except ValueError:
        return -1


def getInput():
    inputText = ""
    try:
        while True:
            line = input()
            inputText += line + "\n"
    except EOFError:
        pass
    return inputText
