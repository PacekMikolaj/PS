import sys

# import os
# print(os.getcwd())

params = sys.argv[1::]


def getFile(fileName):
    with open("./cw2/" + fileName, "r") as file:
        return file.readlines()


def cut(params):
    print(params)
    if len(params) != 3:
        print("Niepoprawna liczba argumentów!")
        return
    if params[0] == "-f":
        f_param(params[1::])
        return
    if params[0] == "-d":
        d_param(params[1::])
        return

    print("Nieprawidłowy parametr!")
    return


def f_param(params):
    text = getFile(params[1])
    params[0] = params[0].split(",")
    for line in text:
        line = line.split(",")

        for index in params[0]:
            textToPrint = line[int(index) - 1].split("\n")[0]

            print(textToPrint, end=" ")
        print("")


def d_param(params):
    print(params)
    text = getFile(params[1])
    separator = params[0]
    for line in text:
        line = line.split(separator)
        for word in line:
            print(word.split("\n")[0], end="\n")


cut(params)
