"""Module for adding students to students.txt"""

# Tommy May
# A01086435

import Student
import crud


def add_student(students_list: list):
    """Creates a new student object and writes it to students_list and students.txt

    POSTCONDITION: if no errors are found the new student object is added to students.txt
    """
    # takes student info input and splits it into a list
    student_info = input('Enter the information for the new student in format:\n'
                         ' FirstName LastName Student# Standing Grades\n')
    student_info = student_info.split()
    try:
        # converts status to a bool and tries to create a new student object
        student_info[3] = crud.convert_to_bool(student_info[3])
        new_student = Student.Student(student_info[0], student_info[1],
                                      student_info[2], student_info[3], student_info[4:])
    except ValueError as e:
        print(e)
    except IndexError:
        print('You did not enter all required fields for the student (FirstName, LastName, Student#, standing)\n')
    else:
        # writes student to students.txt
        file_write(new_student)
        students_list.append(new_student)


def file_write(student: Student):
    """Writes student object to file students.txt

    PARAM: student a student object
    PRECONDITION: student must be a student object
    POSTCONDITION: student is added to file students.txt
    RETURN: True or False depending on if student was successfully added
    """
    with open('students.txt', 'a') as f_obj:
        f_obj.write(str(student))
    print('student added to file')
    return True
