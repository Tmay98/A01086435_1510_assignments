"""crud module"""

# Tommy May
# A01086435

import Student_Read_Write
import Student_Updating
import Student_Updating
import Student_Read_Write


def check_valid_student_number(student_number):
    if not student_number[0] == 'A' or not student_number[1:].isnumeric() or not len(student_number) == 9:
        raise ValueError("You entered an incorrect student number")
    else:
        return True


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


def main():
    selection = 0
    students_list = []
    students_list = Student_Read_Write.file_read()

    while selection != '6':
        selection = input("Select an option in the menu:\n1. Add student\n2. Delete student\n"
                          "3. Calculate class avg\n4. Print class list\n5. Edit student grades\n6: Quit\n")
        if selection == '1':
            Student_Read_Write.add_student(students_list)
        elif selection == '2':
            Student_Updating.file_delete_student(students_list)
        elif selection == '3':
            Student_Read_Write.print_class_average(students_list)
        elif selection == '4':
            Student_Read_Write.print_class_list()
        elif selection == '5':
            Student_Updating.edit_student_grades(students_list)
        elif selection == '6':
            continue
        else:
            print('incorrect option, please input a number between 1 and 5')


if __name__ == "__main__":
    main()
