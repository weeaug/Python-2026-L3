import math
from domains.model import Course, Student

def input_students(students):
    num_of_stus = int(input("Number of students in a class: "))
    for i in range(num_of_stus):
        s_id = input(f"Student {i + 1} ID: ")
        name = input(f"Student {i + 1} Name: ")
        dob = input(f"Student {i + 1} DoB: ")
        students.append(Student(s_id, name, dob))

def input_courses(courses):
    num_of_courses = int(input("Number of courses: "))
    for i in range(num_of_courses):
        c_id = input(f"Course {i + 1} ID: ")
        name = input(f"Course {i + 1} Name: ")
        credits = int(input(f"Course {i + 1} Credits: "))
        courses.append(Course(c_id, name, credits))

def input_marks(courses, students, marks):
    print("\nList of courses:")
    for course in courses:
        print(f"Course ID: {course.id}, Course Name: {course.name}")
    c_id = input("Select a course id to input marks: ")
    if c_id not in marks:
        marks[c_id] = {}
    print(f"Inputting marks for course {c_id}:")
    for student in students:
        s_id = student.id
        raw_mark = float(input(f"Mark for {student.name} (ID: {s_id}): "))
        mark = math.floor(raw_mark * 10) / 10
        marks[c_id][s_id] = mark