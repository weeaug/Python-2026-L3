import math
import numpy as np

students = []
courses = []
marks = {}

def input_students():
    num_of_stus = int(input("Number of students in a class: "))
    for i in range(num_of_stus):
        s_id = input(f"Student {i + 1} ID: ")
        name = input(f"Student {i + 1} Name: ")
        dob = input(f"Student {i + 1} DoB: ")
        students.append({
            "id": s_id,
            "name": name,
            "dob": dob
    })

def input_courses():
    num_of_courses = int(input("Number of courses: "))
    for i in range(num_of_courses):
        c_id = input(f"Course {i + 1} ID: ")
        name = input(f"Course {i + 1} Name: ")
        credits = int(input(f"Course {i + 1} Credits: "))
        courses.append({
            "id": c_id,
            "name": name,
            "credits": credits
    })

def list_students():
    print("List of students: ")
    for student in students:
        print(f"Student ID: {student['id']}, Student Name: {student['name']}, Student DoB: {student['dob']}")

def list_courses():
    print("List of courses: ")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}, Course Credits: {course['credits']}")

def input_marks():
    list_courses()
    c_id = input("Select a course id to input marks: ")
    if c_id not in marks:
        marks[c_id] = {}
    print(f"Inputting marks for course {c_id}:")
    for student in students:
        s_id = student["id"]
        raw_mark = float(input(f"Mark for {student['name']} (ID: {s_id}): "))
        mark = math.floor(raw_mark * 10) / 10
        marks[c_id][s_id] = mark

def show_student_marks():
    list_courses()
    c_id = input("Select a course id to view marks: ")
    if c_id in marks:
        print(f"\nMarks for course {c_id}:")
        for s_id, mark in marks[c_id].items():
            student_name = "Unknown"
            for s in students:
                if s["id"] == s_id:
                    student_name = s["name"]
                    break
            print(f"Student: {student_name} (ID: {s_id}) - Mark: {mark}")
    else:
        print("No marks found for this course.")

def calculate_gpa_and_sort():
    if not students or not courses:
        return
    
    credits_map = {c["id"]: c["credits"] for c in courses}

    for student in students:
        s_id = student["id"]
        student_marks = []
        student_credits = []

        for c_id, course_marks in marks.items():
            if s_id in course_marks:
                student_marks.append(course_marks[s_id])
                student_credits.append(credits_map.get(c_id, 0))
            if student_marks and sum(student_credits) > 0:
                arr_marks = np.array(student_marks, dtype=float)
                arr_credits = np.array(student_credits, dtype=float)
                gpa = np.sum(arr_marks * arr_credits) / np.sum(arr_credits)
            else:
                gpa = 0.0
            
            student["gpa"] = round(float(gpa), 2)

        gpas = np.array([s.get("gpa", 0.0) for s in students])
        sorted_indices = np.argsort(gpas)[::-1]

        print("\nStudents Sorted by GPA (Descending):")
        for idx in sorted_indices:
            s = students[idx]
            print(f"Student: {s['name']} (ID: {s['id']}) - GPA: {s.get('gpa', 0.0)}")

if __name__ == "__main__":
    input_students()
    input_courses()
    list_students()
    for _ in range(len(courses)):
        input_marks()
    show_student_marks()
    calculate_gpa_and_sort()