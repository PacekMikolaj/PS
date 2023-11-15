class Student:
    

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

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
        return self.name + " " + self.surname

    def __eq__(self, other):
        if other == None:
            return False
        return other.name == self.name and other.surname == self.surname
