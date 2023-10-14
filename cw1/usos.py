import sys
import json

with open('./PS/cw1/data.json', 'r') as file:
    data = json.load(file)

math = data['math']
physics = data['physics']

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
    with open('./PS/cw1/data.json', 'w') as file:
        json.dump({ "math": math, "physics": physics }, file)

def main():
    if len(sys.argv) < 2:
        print('Za mało argumentów')
        return

    if str(sys.argv[1]) == '--wykaz_ocen':
        showMarks()
        return

    elif (len(sys.argv) - 1)%3 == 0:
        a = int((len(sys.argv) - 1)/3)

        for i in range(a):
            subject = sys.argv[i*3 + 1]
            student = sys.argv[i*3 + 2]
            mark = sys.argv[i*3 + 3]
         
            if subject != 'Matematyka' and subject != 'Fizyka':
                print('Zła nazwa przedmiotu!')
                return
            
            if not isFloat(mark):
                print ('Niepoprawna ocena!')
                return
            addMark(subject,student,mark)
        showMarks()
    else:
        print('zła liczba argumentów')
        return
    
    saveChanges()


main()