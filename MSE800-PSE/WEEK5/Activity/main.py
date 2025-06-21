from database import create_table, create_course_table, create_user_courses_table
from user_manager import (
    add_user, view_users, search_user, delete_user, advanced_search_user,
    insert_course, assign_course_to_user, search_course_by_user
)

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Advanced Search by ID and Name")
    print("6. Insert Course")
    print("7. Assign Course to User")
    print("8. Search Course by ID and User Name")
    print("9. Exit")

def main():
    create_table()
    create_course_table()
    create_user_courses_table()

    while True:
        menu()
        choice = input("Select an option (1-9): ")
        
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)

        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)

        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)

        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)

        elif choice == '5':
            user_id = int(input("Enter user ID to search: "))
            name = input("Enter name to search: ")
            users = advanced_search_user(user_id, name)
            for user in users:
                print(user)

        elif choice == '6':
            course_id = int(input("Enter course ID: "))
            name = input("Enter course name: ")
            unit = int(input("Enter unit count: "))
            insert_course(course_id, name, unit)

        elif choice == '7':
            user_id = int(input("Enter user ID to assign course to: "))
            course_id = int(input("Enter course ID: "))
            assign_course_to_user(user_id, course_id)

        elif choice == '8':
            course_id = int(input("Enter course ID: "))
            user_name = input("Enter user name to search: ")
            results = search_course_by_user(course_id, user_name)
            for course in results:
                print(course)

        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()