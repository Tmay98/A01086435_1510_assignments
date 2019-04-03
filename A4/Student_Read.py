"""Module for printing info about students in students.txt"""

from Student import Student
import crud


def print_class_average(students_list):
    """Calculates class average and prints it

    POSTCONDITION: if there is 1 or more students calculate the class average and print it
    """
    # returns None if no students are found
    if len(students_list) == 0:
        print('No students in file')
        return None
    # calculate all students average individually and add them to student_average_list
    student_average_list = calculate_each_students_average(students_list)
    # calculates and prints all students combined average to 2 decimal points
    class_average = 0
    for average in student_average_list:
        class_average += int(average)
    if student_average_list:
        class_average = round(class_average / len(student_average_list), 2)
        print("the class average is: %.2f%%\n" % class_average)
    else:
        print('No students with grades found')


def calculate_each_students_average(students_list):
    """Calculates all students averages and returns a list of them

    PARAM: students_list is a list
    PRECONDITION: student list must be a list of correctly formatted students
    POSTCONDITION: all students independent averages are calculated and appended to students_average_list
    RETURN: list with all students averages

    """
    student_average_list = []
    # calculates all students individual averages
    for i in range(0, len(students_list)):
        try:
            if students_list[i].get_gpa() != -1:
                student_average_list.append(students_list[i].get_gpa())
        except ValueError:
            pass
    return student_average_list


def print_class_list():
    """prints the class list

    POSTCONDITION: reads students.txt and prints all lines, excluding empty lines
    """
    try:
        with open("students.txt") as f_obj:
            print('Students list:')
            # loop through all lines in students.txt
            for line in f_obj:
                # if the line isn't empty prints the line
                if line != '\n':
                    print(line)
    except FileNotFoundError:
        print('no students in file\n')


def file_read():
    students_list = []
    try:
        with open('students.txt') as f_obj:
            for line in f_obj:
                if line != '\n':
                    line = line.split()
                    line[3] = crud.convert_to_bool(line[3])
                    students_list.append(Student(line[0], line[1], line[2], line[3], line[4:]))
    except FileNotFoundError:
        return []
    else:
        return students_list
