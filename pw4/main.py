from input import input_courses, input_marks, input_students
from output import (
    calculate_gpa_and_sort,
    list_courses,
    list_students,
    show_student_marks,
)

students = []
courses = []
marks = {}

if __name__ == "__main__":
    input_students(students)
    input_courses(courses)
    list_students(students)
    list_courses(courses)

    for _ in range(len(courses)):
        input_marks(courses, students, marks)

    show_student_marks(courses, students, marks)
    calculate_gpa_and_sort(courses, students, marks)