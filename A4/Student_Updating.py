"""Module for updating / deleting students from students.txt and students list"""

# Tommy May
# A01086435


def file_delete_student(students_list) -> bool:
    """Asks for a student number and deletes the student from file students.txt

    POSTCONDITION: the specified student is deleted from file if it is found
    RETURN: True if student is deleted, False if the student wasnt found
    """
    # Asks for student number to delete
    delete_student_number = input('Enter the student number of the student to be deleted\n')
    try:
        # checks if user input was a valid student number and raises an error if it is invalid
        check_valid_student_number(delete_student_number)
        # deletes student from students_list. raises value error if no students exist
        delete_student_in_memory(students_list, delete_student_number)
    except ValueError as e:
        print(e)
        return False
    else:
        # rewrites students to students.txt with changes
        print('Student deleted successfully')
        file_write_changes(students_list)
        return True


def delete_student_in_memory(students_list, delete_student_number):
    for i in range(len(students_list)):
        if students_list[i].get_student_number() == delete_student_number:
            del students_list[i]
            return
    raise ValueError('Student does not exist')


def edit_student_grades(students_list):
    """Asks for student number to add grades to and if the student exists allows user to add grades.

    POSTCONDITION: if student is found asks user for grades and adds them all to student
    RETURN: True if student is on file, False otherwise
    """
    student_number = input('Enter the student number of the student to add grades to\n')
    try:
        # checks if user input was a valid student number and raises an error if it is invalid
        check_valid_student_number(student_number)
        # returns index where student is in students_list
        student_location = find_student(student_number, students_list)
        # loops through asking user to input grades
        add_grades_to_student(student_location, students_list)
        # rewrites student to students.txt with changes
        file_write_changes(students_list)
    except ValueError as e:
        print(e)
        return False
    except FileNotFoundError:
        print('File students.txt does not exist')
        return False
    return True


def find_student(student_number, students_list):
    index = 0
    for student in students_list:
        if student.get_student_number() == student_number:
            return index
        index += 1
    raise ValueError('Student does not exist')


def add_grades_to_student(student_location, students_list):
    while True:
        try:
            # converts grade input to int
            grade = int(input('Enter a grade between 0 and 100'
                              ' to add to student type anything else to stop adding\n').strip())
        except ValueError:
            print('non integer grade entered, exiting edit\n')
            break
        # checks if grade is above 100 or below 0. exits loop and prints error message if it is
        if grade < 0 or grade > 100:
            print('You entered a grade below 0 or above 100, exiting edit\n')
            break
        # writes the grade to students list if no errors
        else:
            students_list[student_location].add_grade(str(grade))
    print('All valid grades were added to the student')


def file_write_changes(students_list):
    with open('students.txt', 'w') as f_obj:
        for student in students_list:
            f_obj.write(str(student))


def check_valid_student_number(student_number):
    if not student_number[0] == 'A' or not student_number[1:].isnumeric() or not len(student_number) == 9:
        raise ValueError("You entered an incorrect student number")
    else:
        return True