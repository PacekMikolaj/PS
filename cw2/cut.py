import sys
import supportScripts

params = sys.argv[1::]


def cut(params):
    text = supportScripts.getInput()
    if len(params) % 2 != 0:
        return "Error!"
    if supportScripts.checkIfParamIsUsed("-d", params) != -1:
        text = d_param(
            text.split("\n"),
            params[supportScripts.checkIfParamIsUsed("-d", params) + 1],
        )
    if supportScripts.checkIfParamIsUsed("-f", params) != -1:
        text = f_param(
            text.split("\n"),
            params[supportScripts.checkIfParamIsUsed("-f", params) + 1].split(","),
        )
    return text


def f_param(text, columns):
    outputText = ""
    for line in text:
        line = line.split(" ")
        for index in columns:
            textToPrint = line[int(index) - 1].split("\n")[0]

            outputText += textToPrint + " "
        outputText += "\n"

    return outputText


def d_param(text, separator):
    outputText = ""

    for line in text:
        line = line.split(separator)
        for word in line:
            outputText += word.split("\n")[0] + " "
        outputText += "\n"

    return outputText


# print(cut(params))
