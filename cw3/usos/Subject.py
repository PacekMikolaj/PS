class Subject:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        self.marks = { 'Marcinek': [], 'Mikolajek': [] }

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name

    def add(self, student, mark):
        print(student.name,mark)
        try:
            self.marks[student.name].append(mark)
        except:
            print('Podany student nie jest zapisany na ten przedmiot!')


    