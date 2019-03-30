"""Module for printing info about students in students.txt"""


def print_class_average():
    """Calculates class average and prints it

    POSTCONDITION: if there is 1 or more students calculate the class average and print it
    """
    students_list = file_read()
    # checks if file is empty
    if len(students_list) == 0:
        print('No students in file')
        return
    # calculate all students average individually and add them to student_average_list
    student_average_list = calculate_students_average(students_list)
    # calculates and prints all students combined average
    class_average = 0
    for average in student_average_list:
        class_average += int(average)
    if student_average_list:
        class_average = round(class_average / len(student_average_list), 2)
        print("the class average is:", class_average, "%\n")
    else:
        print('No students with grades found')


def calculate_students_average(students_list):
    """Calculates all students averages and returns a list of them

    PARAM: students_list is a list
    PRECONDITION: student list must be a list of correctly formatted students
    POSTCONDITION: all students independent averages are calculated and appended to students_average_list
    RETURN: list with all students averages

    """
    student_average_list = []
    # calculates all students individual averages
    for i in range(0, len(students_list)):
        student = students_list[i].split()
        total_grades = 0
        # checks if student has any grades
        if len(student) > 4:
            # calculates the average and appends it to students_average_list
            for j in range(4, len(student)):
                total_grades += int(student[j])
            student_average_list.append(total_grades / (len(student) - 4))
    return student_average_list


def print_class_list():
    """prints the class list

    POSTCONDITION: reads students.txt and prints all lines, excluding empty lines
    """
    try:
        with open("students.txt") as f_obj:
            print('Students list:')
            for line in f_obj:
                # if the line isn't empty prints the line
                if line != '\n':
                    print(line)
    except FileNotFoundError:
        print('no students in file\n')


def file_read() -> list:
    """Reads students.txt file and returns it as a list

    POSTCONDITION: students.txt is read and added to students_list
    RETURN: list of all students or empty list if no students
    """
    try:
        with open("students.txt") as f_obj:
            students_list = f_obj.readlines()
    except FileNotFoundError:
        print('no students in file\n')
        return []
    else:
        if len(students_list) > 0:
            return students_list
        return []
