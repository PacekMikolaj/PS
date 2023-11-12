class Subject:
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return self.name

    def __str__(self):
        return self.name + "\n\t"

    def __eq__(self, other):
        if other == None:
            return False
        return other.name == self.name

    # def add(self, student, mark):
    #     print(student.name, mark)
    #     try:
    #         for selfStudent in self.students:
    #             if selfStudent.name == student.name:
    #                 student.add(self.name, mark)
    #     except:
    #         print("Podany student nie jest zapisany na ten przedmiot!")

    # def remove(self, student, markIndex):
    #     print(student.name, markIndex)
    #     try:
    #         for selfStudent in self.students:
    #             if selfStudent.name == student.name:
    #                 student.remove(self.name, markIndex)
    #     except:
    #         print("Podany student nie jest zapisany na ten przedmiot!")
