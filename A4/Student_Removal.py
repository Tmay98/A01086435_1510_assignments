"""Module for deleting a student from students.txt"""

# Tommy May
# A01086435

import Student


def file_delete_student() -> bool:
    """Asks for a student number and deletes the student from file students.txt

    POSTCONDITION: the specified student is deleted from file if it is found
    RETURN: True if student is deleted, False if the student wasnt found
    """
    # Asks for student number to delete
    delete_student_number = input('Enter the student number of the student to be deleted\n')
    try:
        # checks if user input was a valid student number and raises an error if it is invalid
        Student.check_valid_student_number(delete_student_number)
    except ValueError as e:
        print(e)
        return False
    with open("students.txt", "r+") as f_obj:
        # reads students.txt into the string lines and checks if the specified student exists
        lines = f_obj.readlines()
        f_obj.seek(0)
        if delete_student_number in str(lines):
            delete_student_in_file(f_obj, lines, delete_student_number)
            return True
        print('student not found')
        return False


def delete_student_in_file(f_obj, lines: list, delete_student_number: str):
    """Goes through file line by line rewriting only students without student number to delete

    PARAM: f_obj a file object
    PRECONDITION: f_obj must be a file object
    PARAM: lines a list
    PRECONDITION: lines must be a list of student info
    PARAM delete_student_number: a string
    PRECONDITION: delete_student_number is a string with a valid student number
    POSTCONDITION: the specified student number is deleted from the file
    """
    # writes all students to students.txt except the one to delete
    for line in lines:
        if delete_student_number not in str(line):
            f_obj.write(line)
    f_obj.truncate()
    print('Student deleted successfully')
