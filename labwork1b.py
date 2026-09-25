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
        courses.append({
            "id": c_id,
            "name": name
    })

def list_students():
    print("List of students: ")
    for student in students:
        print(f"Student ID: {student['id']}, Student Name: {student['name']}, Student DoB: {student['dob']}")

def list_courses():
    print("List of courses: ")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

def input_marks():
    list_courses()
    c_id = input("Select a course id to input marks: ")
    if c_id not in marks:
        marks[c_id] = {}
    print(f"Inputting marks for course {c_id}:")
    for student in students:
        s_id = student["id"]
        mark = float(input(f"Mark for {student['name']} (ID: {s_id}): "))
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

if __name__ == "__main__":
    input_students()
    input_courses()
    list_students()
    list_courses()
    for _ in range(len(courses)):
        input_marks()
    show_student_marks()