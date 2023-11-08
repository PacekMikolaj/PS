class Student:

    id = 0
    def __init__(self, name,surname):
        self.name = name
        self.surname = surname
        self.id = id
        id+=1

    def add(self, subjectName, mark):
        try:
            self.marks[subjectName].append(mark)
        except:
            self.marks[subjectName] = []
            self.marks[subjectName].append(mark)

    def remove(self, subjectName, markIndex):
        try:
            del self.marks[subjectName][int(markIndex) - 1]
        except:
            print("Brak oceny o podanym indeksie")

    def __repr__(self):
        return self.name

    def __str__(self):
        returnString = self.name + "\n\t"
        for key in self.marks.keys():
            returnString += key + "\t"
            for mark in self.marks[key]:
                returnString += str(mark) + " "
            returnString += "\n\t"
        return returnString

    def __eq__(self, other):
        if not isinstance(other, Student):
            return TypeError
        return other.id == self.id
