class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        """Display the student's information."""
        print(f"Name: {self.name}\nAge: {self.age}\nGrades: {self.grades}")

    def calculate_average_grade(self):
        """Calculate and return the average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grades):
        """Add a new student to the database."""
        new_student = Student(name, age, grades)
        self.students.append(new_student)
        print(f"Student {name} added successfully!\n")

    def display_all_students(self):
        """Display information for all students."""
        if not self.students:
            print("No students in the database.")
            return
        for student in self.students:
            student.display_info()
            print(f"Average Grade: {student.calculate_average_grade():.2f}\n")

# Simulating user interactions


def main():
    print("Welcome to the Student Database System!\n")
    db = StudentDatabase()

    while True:
        print("Options:\n1. Add a new student\n2. Display all students\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grades = list(
                map(int, input("Enter student's grades (separated by spaces): ").split()))
            db.add_student(name, age, grades)
        elif choice == "2":
            db.display_all_students()
        elif choice == "3":
            print("Exiting the Student Database System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()