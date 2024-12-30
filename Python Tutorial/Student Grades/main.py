import os


def input_student_grade():
    grades_list = []

    while True:
        try:
            subject = input(
                "Enter your signed subject names then enter 'done' to save\n")
            if subject.upper() == 'DONE':
                break

            subject_grade = float(
                input(f"Enter grade for subject {subject}: "))
            if subject_grade < 0 or subject_grade > 100:
                print("Grade must be between 0 and 100. Please enter a valid grade.")
                continue

            grades_list.append((subject, subject_grade))

        except ValueError:
            print("Invalid input. Please enter a valid numeric grade.")

    return grades_list


def calculate_avg(grades_list):
    if len(grades_list) == 0:
        print("No grades entered. Cannot calculate average.")
        return None
    total_grades = sum(grade for subject, grade in grades_list)
    avg = total_grades / len(grades_list)
    return avg


def store_grades(file_name, grade_list):
    try:
        with open(file_name, "a") as my_file:
            for subject, grade in grade_list:
                my_file.write(f"{subject}: {grade}\n")
    except IOError:
        print("Error writing to file.")


def read_grades_from_file(file_name):
    if not os.path.exists(file_name):
        print("No previous grades found.")
        return None

    grade_list = []
    try:
        with open(file=file_name, mode='r') as my_file:
            for line in my_file:
                subject, grade = line.strip().split(": ")
                grade_list.append((subject, float(grade)))
    except IOError:
        print("Error reading from file.")
    except ValueError:
        print("Error processing grades in the file.")

    return grade_list


def main():
    print("Welcome to the Student Grade Tracker")

    file_name = "grades.txt"
    grades = read_grades_from_file(file_name)

    new_grades = input_student_grade()

    grades.extend(new_grades)

    store_grades(file_name, new_grades)

    average = calculate_avg(grades)
    if average is not None:
        print(f"The average grade is: {average:.2f}")

    print("\nAll grades:")
    for subject, grade in grades:
        print(f"{subject}: {grade}")


main()