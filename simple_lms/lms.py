class Student:
    def __init__(self, name, email, father_name, semester):
        self.name = name
        self.email = email
        self.father_name = father_name
        self.semester = semester

    def __repr__(self):
        return f"Student(Name: {self.name}, Email: {self.email}, Father: {self.father_name}, Semester: {self.semester})"

# Initial data: 5 students
students = [
    Student("Alice Smith", "alice@example.com", "John Smith", "3rd"),
    Student("Bob Jones", "bob@example.com", "Robert Jones", "1st"),
    Student("Charlie Brown", "charlie@example.com", "Peter Brown", "5th"),
    Student("David Wilson", "david@example.com", "James Wilson", "2nd"),
    Student("Eva Davis", "eva@example.com", "Michael Davis", "4th")
]

def add_student(name, email, father_name, semester):
    new_student = Student(name, email, father_name, semester)
    students.append(new_student)
    print(f"Student {name} added successfully.")

def search_student(query):
    results = [s for s in students if query.lower() in s.name.lower() or query.lower() in s.email.lower()]
    return results

def remove_student(email):
    global students
    original_count = len(students)
    students = [s for s in students if s.email.lower() != email.lower()]
    if len(students) < original_count:
        print(f"Student with email {email} removed successfully.")
        return True
    else:
        print(f"No student found with email {email}.")
        return False

def display_students():
    if not students:
        print("No students in the system.")
    else:
        print("\n--- Student List ---")
        for i, s in enumerate(students, 1):
            print(f"{i}. {s}")
        print("--------------------")

def main():
    while True:
        print("\n--- Simple LMS Menu ---")
        print("1. Display All Students")
        print("2. Add Student")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_students()
        elif choice == '2':
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            father_name = input("Enter Father's Name: ")
            semester = input("Enter Semester: ")
            add_student(name, email, father_name, semester)
        elif choice == '3':
            query = input("Enter Name or Email to search: ")
            results = search_student(query)
            if results:
                print(f"\n--- Search Results for '{query}' ---")
                for s in results:
                    print(s)
            else:
                print(f"No students found matching '{query}'.")
        elif choice == '4':
            email = input("Enter Email of student to remove: ")
            remove_student(email)
        elif choice == '5':
            print("Exiting LMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
