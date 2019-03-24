"""crud module"""

# Tommy May
# A01086435

import Student


def main():
    selection = 0
    while selection != '5':
        selection = input("Select an option in the menu:\n1. Add student\n2. Delete student\n"
                          "3. Calculate class avg\n4. Print class list\n5. Quit")
        if selection == '1':
            student_info = input('Enter the information for the new student in format:\n'
                                 ' FirstName LastName Student# Standing Grades')
            Student.add_student(student_info)
        elif selection == '2':
            delete_student = input('Enter the student number of the student to be deleted')
            student_deleted = Student.file_delete_student(delete_student)
            if student_deleted:
                print('student deleted successfully')
            else:
                print('student not found')
        elif selection == '3':
            Student.calculate_class_average()
        elif selection == '4':
            Student.print_class_list()
        elif selection == '5':
            continue
        else:
            print('incorrect option, please input a number between 1 and 5')



if __name__ == "__main__":
    main()
