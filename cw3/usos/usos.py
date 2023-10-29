from Subject import Subject
from Student import Student


def main():
    list_of_students = [Student("Jak Kowalski"), Student("Anna Kowalska")]
    list_of_subjects = [
        Subject("Matematyka", [list_of_students[0]]),
        Subject("Fizyka", list_of_students),
    ]

    print(list_of_subjects)

    list_of_subjects[0].add(list_of_students[0], 3.0)
    list_of_subjects[0].add(list_of_students[0], 3.5)
    list_of_subjects[1].add(list_of_students[0], 5.0)

    print(list_of_subjects[0])
    print(list_of_students)
    list_of_subjects[0].remove(list_of_students[0], 5)
    print(list_of_students[0])


main()
