import numpy as np

def list_students(students):
    print("List of students: ")
    for student in students:
        print(f"Student ID: {student.id}, Student Name: {student.name}, Student DoB: {student.dob}")

def list_courses(courses):
    print("List of courses: ")
    for course in courses:
        print(f"Course ID: {course.id}, Course Name: {course.name}, Course Credits: {course.credits}")

def show_student_marks(courses, students, marks):
    list_courses(courses)
    c_id = input("Select a course id to view marks: ")
    if c_id in marks:
        print(f"\nMarks for course {c_id}:")
        for s_id, mark in marks[c_id].items():
            student_name = "Unknown"
            for s in students:
                if s.id == s_id:
                    student_name = s.name
                    break
            print(f"Student: {student_name} (ID: {s_id}) - Mark: {mark}")
    else:
        print("No marks found for this course.")

def calculate_gpa_and_sort(courses, students, marks):
    if not students or not courses:
        return
    
    credits_map = {c.id: c.credits for c in courses}

    for student in students:
        s_id = student.id
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
            
            student.gpa = round(float(gpa), 2)

        gpas = np.array([getattr(s, "gpa", 0.0) for s in students])
        sorted_indices = np.argsort(gpas)[::-1]

        print("\nStudents Sorted by GPA (Descending):")
        for idx in sorted_indices:
            s = students[idx]
            print(f"Student: {s.name} (ID: {s.id}) - GPA: {s.gpa}")