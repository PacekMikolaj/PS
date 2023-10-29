class Subject:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        self.maxStudents = 2

    def __repr__(self):
        return self.name

    def __str__(self):
        returnString = self.name + "\n\t"
        returnString += "Maksymalna liczba studentów: " + str(self.maxStudents) + "\n\t"
        returnString += "Aktualna liczba studentów: " + str(len(self.students)) + "\n\t"
        returnString += "Zapisani studenci: \n\t\t"
        for student in self.students:
            returnString += student.name + "\n\t\t"
        return returnString

    def add(self, student, mark):
        print(student.name, mark)
        try:
            for selfStudent in self.students:
                if selfStudent.name == student.name:
                    student.add(self.name, mark)
        except:
            print("Podany student nie jest zapisany na ten przedmiot!")

    def remove(self, student, markIndex):
        print(student.name, markIndex)
        try:
            for selfStudent in self.students:
                if selfStudent.name == student.name:
                    student.remove(self.name, markIndex)
        except:
            print("Podany student nie jest zapisany na ten przedmiot!")
