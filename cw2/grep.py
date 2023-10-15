import sys

# import os
# print(os.getcwd())

params = sys.argv[1::]


def getFile(fileName):
    with open("./cw2/" + fileName, "r") as file:
        return file.readlines()


def grep(params):
    print(params)
    if len(params) != 3:
        print("Niepoprawna liczba argumentów!")
        return
    if params[0] == "-i":
        i_param(params[1::])
        return
    if params[0] == "-w":
        w_param(params[1::])
        return

    print("Nieprawidłowy parametr!")
    return


def i_param(params):
    text = getFile(params[1])
    textToCompare = params[0]

    for line in text:
        if textToCompare.lower() in line.lower():
            print(line.split("\n")[0], end="")
        print("")


def w_param(params):
    text = getFile(params[1])
    textToCompare = params[0]

    for line in text:
        flag = False
        for word in line.split(","):
            if textToCompare == word.split("\n")[0]:
                flag = True
                break
        if flag:
            print(line)


grep(params)
