with open("./cw2/usos.txt", "r") as file:
    data = file.readlines()

math = []
physics = []


def readDataFromFile(data):
    subjectUsed = "math"
    for line in data:
        if len(line.split(":")) > 1:
            # dodawanie
            line = line.split(":")
            if subjectUsed == "math":
                # delete enter in the end
                line[-1] = line[-1][:-1]
                math.append([line[0], line[1:]])
                math[-1][1][-1] = math[-1][1][-1].split("\n")[0]
            else:
                physics.append([line[0], line[1:]])
                physics[-1][1][-1] = physics[-1][1][-1].split("\n")[0]
        else:
            if line == "__MATEMATYKA__\n":
                subjectUsed = "math"
            else:
                subjectUsed = "fizyka"


readDataFromFile(data)


def printMark(arg, index):
    [student, marks] = arg
    print(index + 1, end="")
    print(".", student, end=" ")
    for mark in marks:
        print(mark, end=" ")
    print("")
    return


def showMarks():
    print(
        """
----------+----------+-------+ 
Przedmiot | Studenci | Oceny |
----------+----------+-------+ 
    """
    )
    if len(math) > 0:
        print("Matematyka: ")
        for index, i in enumerate(math):
            printMark(i, index)
        print("")
    if len(physics) > 0:
        print("Fizyka: ")
        for index, i in enumerate(physics):
            printMark(i, index)
    return


def addMark(subject, student, mark):
    studentExist = -1
    if subject == "Matematyka":
        for i in range(len(math)):
            if math[i][0] == student:
                studentExist = i
                break
        if studentExist != -1:
            math[studentExist][1].append(mark)
        else:
            math.append([student, [mark]])
    else:
        for i in range(len(physics)):
            if physics[i][0] == student:
                studentExist = i
                break
        if studentExist != -1:
            physics[studentExist][1].append(mark)
        else:
            physics.append([student, [mark]])


def deleteMark(subject, student, markIndex):
    studentExist = -1
    if subject == "Matematyka":
        for i in range(len(math)):
            if math[i][0] == student:
                studentExist = i
                break
        if studentExist != -1:
            if markIndex < len(math[studentExist][1]):
                del math[studentExist][1][markIndex]
            else:
                print("Ocena nie istnieje!")
        else:
            print("Podany student nie istnieje!")
    else:
        for i in range(len(physics)):
            if physics[i][0] == student:
                studentExist = i
                break
        if studentExist != -1:
            if markIndex < len(math[studentExist][1]):
                del physics[studentExist][1][int(markIndex)]
            else:
                print("Ocena nie istnieje!")
        else:
            print("Podany student nie istnieje!")


def saveChanges():
    returnText = ""
    returnText += "__MATEMATYKA__\n"
    for studentAndMarks in math:
        [student, marks] = studentAndMarks
        returnText += student
        for mark in marks:
            returnText += ":" + mark
        returnText += "\n"

    returnText += "__FIZYKA__\n"
    for studentAndMarks in physics:
        [student, marks] = studentAndMarks
        returnText += student
        for mark in marks:
            returnText += ":" + mark
        returnText += "\n"

    with open("./cw2/usos.txt", "w") as file:
        file.write(returnText)


def getInput():
    inputText = ""
    try:
        while True:
            line = input()
            inputText += line + "\n"
    except EOFError:
        pass
    return inputText


def main():
    inputData = getInput().split("\n")


    for line in inputData:
        if line == "grades":
            showMarks()
            continue
        if line != "":
            try:
                if "+" in line:
                    student = line.split("+")[0]
                else:
                    student = line.split("-")[0]
                SaM = line.split("=")[1].split("|")
                for subjectAndMarks in SaM:
                    subject = subjectAndMarks.split("(")[0]
                    marks = subjectAndMarks.split("(")[1].split(")")[0].split(",")

                    for mark in marks:
                        if "+" in line:
                            addMark(subject, student, mark.split("\n")[0])
                        else:
                            deleteMark(subject, student, mark)
            except:
                print("Błąd składni!")
                return
    saveChanges()


main()
