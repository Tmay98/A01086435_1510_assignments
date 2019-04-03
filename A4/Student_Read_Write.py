"""Module for printing and reading info about students in students.txt"""

# Tommy May
# A01086435

from Student import Student


def print_class_average(students_list):
    """Calculates class average and prints it

    PARAM: students_list a list of student objects
    PRECONDITION: students_list must be a list of student objects
    POSTCONDITION: if there is 1 or more students calculate the class average and print it
    RETURN: None if no students found
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

    PARAM: students_list a list of student objects
    PRECONDITION: students_list must be a list of student objects
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
    """Prints the class list

    POSTCONDITION: reads students.txt and prints all lines, excluding empty lines.
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
    """ Reads students.txt and creates student objects from it and appends them to students_list

    POSTCONDITION: all students from students.txt added to students_list
    """
    students_list = []
    try:
        with open('students.txt') as f_obj:
            for line in f_obj:
                if line != '\n':
                    line = line.split()
                    line[3] = convert_to_bool(line[3])
                    students_list.append(Student(line[0], line[1], line[2], line[3], line[4:]))
    except FileNotFoundError:
        return []
    else:
        return students_list


def add_student(students_list: list):
    """Creates a new student object and writes it to students_list and students.txt

    PARAM: students_list a list of student objects
    PRECONDITION: students_list must be a list of student objects
    POSTCONDITION: if no errors are found the new student object is added to students.txt and students_list
    """
    # takes student info input and splits it into a list
    student_info = input('Enter the information for the new student in format:\n'
                         ' FirstName LastName Student# Standing Grades\n')
    student_info = student_info.split()
    try:
        # converts status to a bool and tries to create a new student object
        student_info[3] = convert_to_bool(student_info[3])
        # raises an error if student number already exists
        check_if_student_number_exists(student_info[2], students_list)
        # creates new student object
        new_student = Student(student_info[0], student_info[1],
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
    """
    with open('students.txt', 'a') as f_obj:
        f_obj.write(str(student))
    print('student added to file')


def check_if_student_number_exists(student_number, students_list):
    """Goes through students_list and raises a ValueError if student_number is inside it\

    PARAM: students_list a list of student objects
    PRECONDITION: students_list must be a list of student objects
    PARAM: student_number is a string
    PRECONDITION: student_number is a correctly formatted student number
    POSTCONDITION: raises ValueError if student_number exists
    """
    for student in students_list:
        if student.get_student_number() == student_number:
            raise ValueError('A student with that student number already exists')


def convert_to_bool(status: str) -> bool:
    """converts a string to a bool

    PARAM: status a string
    PRECONDITION: status must be a string
    POSTCONDITION: status is converted to a bool
    RETURN: the converted bool value
    """
    status = status.capitalize()
    if status == 'True':
        return True
    elif status == 'False':
        return False
    else:
        raise ValueError('You entered an incorrect status')
