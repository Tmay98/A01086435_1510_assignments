"""crud module"""

# Tommy May
# A01086435

import Student_Updating
import Student_Read_Write


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
