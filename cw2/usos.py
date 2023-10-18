import sys
import json

with open('./cw2/usos.txt', 'r') as file:
    # data = json.load(file)
    data = file.readlines()

math = []
physics = []

def readDataFromFile(data):
    subjectUsed = 'math'
    for line in data:
        if len(line.split(':')) > 1:
            # dodawanie   
            line = line.split(':')
            if subjectUsed == 'math':
                # delete enter in the end
                line[-1] = line[-1][:-1]
                math.append([line[0],line[1:]])
            else:
                physics.append([line[0],line[1:]])
        else:
            if line == "__MATEMATYKA__\n":
                subjectUsed = 'math'
            else:
                subjectUsed = 'fizyka'

readDataFromFile(data)

def printMark(arg, index):
    [student, marks ] = arg
    print(index + 1,end='')
    print('.', student,end=' ')
    for mark in marks:
        print(mark, end=' ')
    print('')
    return
   

def showMarks():
    print('''
----------+----------+-------+ 
Przedmiot | Studenci | Oceny |
----------+----------+-------+ 
    ''')
    if len(math) > 0:
        print('Matematyka: ')
        for index, i in enumerate(math):
            printMark(i,index)
        print('')
    if len(physics) > 0:
        print('Fizyka: ')
        for  index, i in enumerate(physics):
                    printMark(i,index)
    return

def addMark(subject,student,mark):
    studentExist = False
    if (subject == 'Matematyka'):
        for i in range(len(math)):
            if math[i][0] == student: 
                studentExist = i
                break
        if studentExist != False:
            math[studentExist][1].append(mark)
        else:
            math.append([ student, [mark] ])
    else: 
        for i in range(len(physics)):
            if physics[i][0] == student:
                studentExist = i
                break
        if studentExist != False:
            physics[studentExist][1].append(mark)
        else:
            physics.append([ student, [mark] ])

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def saveChanges():
    returnText = ""
    returnText += "__MATEMATYKA__\n"
    for studentAndMarks in math:
        [ student, marks ] = studentAndMarks
        returnText += student
        for mark in marks:
            returnText += ':' + mark 
        returnText += '\n'

    returnText += "__FIZYKA__\n"
    for studentAndMarks in physics:
        [ student, marks ] = studentAndMarks
        returnText += student + ':'
        for mark in marks:
            returnText += ':' + mark 
        returnText += '\n'

    with open('./cw2/text.txt', 'w') as file:
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
    inputData = getInput()
    print(inputData)

    for line in inputData:
        student = line.split('+')[0]
        subjectAndMarks = line.split('=')[1].split('|')
        subject = subjectAndMarks.split('(')[0]
        marks = subjectAndMarks.split('(')[1].split(')')[0].split(',')
        
            # addMark(subject,student,mark)
    #     showMarks()
    # else:
    #     print('zła liczba argumentów')
    #     return
    
    saveChanges()

# showMarks()
# saveChanges()
main()