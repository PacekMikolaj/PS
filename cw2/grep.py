import sys
import supportScripts

params = sys.argv[1::]


def getTextToCompare(params):
    indexToCheck = -1
    if ".txt" in params[-1]:
        indexToCheck = -2
    if params[indexToCheck] != "-i" and params[indexToCheck] != "-w":
        return params[indexToCheck]
    else:
        return "Error"


def grep(params):
    text = supportScripts.getInput()
    textToCompare = getTextToCompare(params)
    lower = False
    if textToCompare == "Error":
        return "Błąd!"
    if supportScripts.checkIfParamIsUsed("-i", params) != -1:
        lower = True
    if supportScripts.checkIfParamIsUsed("-w", params) != -1:
        return w_param(text.split("\n"), textToCompare, lower)
    return classicCompare(text.split("\n"), textToCompare, lower)


def classicCompare(text, textToCompare, lower):
    outputText = ""

    for line in text:
        if lower:
            if textToCompare.lower() in line.lower():
                outputText += line.split("\n")[0]
        else:
            if textToCompare in line:
                outputText += line.split("\n")[0]
        outputText += "\n"
    return outputText


def w_param(text, textToCompare, lower):
    outputText = ""

    for line in text:
        flag = False
        for word in line.split(" "):
            if lower:
                if textToCompare.lower() == word.split("\n")[0].lower():
                    flag = True
                    break
            else:
                if textToCompare == word.split("\n")[0]:
                    flag = True
                    break
        if flag:
            outputText += line + "\n"
    return outputText


# print(grep(params))
