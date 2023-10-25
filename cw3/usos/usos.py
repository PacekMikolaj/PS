from Subject import Subject
from Student import Student

def main():

    list_of_students = [ Student('Marcinek'), Student('Pawelek'), Student('Mikolajek')]
    list_of_subjects = [ Subject('Matematyka',list_of_students), Subject('Fizyka', list_of_students) ]


    print(list_of_subjects)

    list_of_subjects[0].add(list_of_students[0],3.0)

    # print()

main()
