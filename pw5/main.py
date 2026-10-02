import os
import zipfile
from domains.model import Course, Student
from input import input_courses, input_marks, input_students
from output import (
    calculate_gpa_and_sort,
    list_courses,
    list_students,
    show_student_marks,
)

def load_data(students, courses, marks):
    if os.path.exists("students.dat"):
        print("Found students.dat, decompressing...")
        with zipfile.ZipFile("students.dat", "r") as zf:
            zf.extractall(".")

    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], parts[2]))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                    if c_id not in marks:
                        marks[c_id] = {}
                    marks[c_id][s_id] = mark
    print("Data loaded successfully!")

def save_and_compress():
    print("Compressing files into students.dat...")
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zf:
        if os.path.exists("students.txt"):
            zf.write("students.txt")
        if os.path.exists("courses.txt"):
            zf.write("courses.txt")
        if os.path.exists("marks.txt"):
            zf.write("marks.txt")
    print("Done! Goodbye.")

def main():
    students = []
    courses = []
    marks = {}

    load_data(students, courses, marks)

    while True:
        print("\n--- Practical Work 5 ---")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Student Marks")
        print("7. Exit")

        choice = input("Select an option (1-7): ")

        if choice == "1":
            input_students(students)
        elif choice == "2":
            input_courses(courses)
        elif choice == "3":
            input_marks(courses, students, marks)
        elif choice == "4":
            list_students(students)
        elif choice == "5":
            list_courses(courses)
        elif choice == "6":
            show_student_marks(courses, students, marks)
        elif choice == "7":
            save_and_compress() 
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
