"""crud module"""

# Tommy May
# A01086435

import Student_Creation
import Student_Updating
import Student_Removal
import Student_Read


def main():
    selection = 0
    while selection != '6':
        selection = input("Select an option in the menu:\n1. Add student\n2. Delete student\n"
                          "3. Calculate class avg\n4. Print class list\n5. Edit student grades\n6: Quit\n")
        if selection == '1':
            Student_Creation.add_student()
        elif selection == '2':
            Student_Removal.file_delete_student()
        elif selection == '3':
            Student_Read.print_class_average()
        elif selection == '4':
            Student_Read.print_class_list()
        elif selection == '5':
            Student_Updating.edit_student_grades()
        elif selection == '6':
            continue
        else:
            print('incorrect option, please input a number between 1 and 5')


if __name__ == "__main__":
    main()
