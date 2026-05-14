import csv
import os

FILE_NAME = "students.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "Marks"])


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!\n")


def search_student():
    roll = input("Enter Roll Number to Search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            if row[0] == roll:
                print("\nStudent Found:")
                print("Roll No:", row[0])
                print("Name:", row[1])
                print("Marks:", row[2])
                found = True
                break

    if not found:
        print("Student not found!\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    students = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        students = list(reader)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        for row in students:
            if row[0] != roll:
                writer.writerow(row)
            else:
                found = True

    if found:
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")


def display_all():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_all()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")