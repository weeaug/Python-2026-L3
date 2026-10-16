class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""

    def input(self, index):
        self.__id = input(f"Student {index} ID: ")
        self.__name = input(f"Student {index} Name: ")
        self.__dob = input(f"Student {index} DoB: ")

    def list(self):
        print(f"Student ID: {self.__id}, Student Name: {self.__name}, Student DoB: {self.__dob}")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""

    def input(self, index):
        self.__id = input(f"Course {index} ID: ")
        self.__name = input(f"Course {index} Name: ")

    def list(self):
        print(f"Course ID: {self.__id}, Course Name: {self.__name}")

    def _get_id(self):
        return self.__id

    def _get_name(self):
        return self.__name
    
class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_of_stus = int(input("Number of students in a class: "))
        for i in range(num_of_stus):
            student = Student()
            student.input(i + 1)
            self.students.append(student)

    def input_courses(self):
        num_of_courses = int(input("Number of courses: "))
        for i in range(num_of_courses):
            course = Course()
            course.input(i + 1)
            self.courses.append(course)

    def list_students(self):
        print("List of students: ")
        for student in self.students:
            student.list()

    def list_courses(self):
        print("List of courses: ")
        for course in self.courses:
            course.list()

    def input_marks(self):
        self.list_courses()
        c_id = input("Select a course id to input marks: ")
        if c_id not in self.marks:
            self.marks[c_id] = {}
        print(f"Inputting marks for course {c_id}:")
        for student in self.students:
            s_id = student.get_id()
            mark = float(input(f"Mark for {student.get_name()} (ID: {s_id}): "))
            self.marks[c_id][s_id] = mark

    def show_student_marks(self):
        self.list_courses()
        c_id = input("Select a course id to view marks: ")
        if c_id in self.marks:
            print(f"\nMarks for course {c_id}:")
            for s_id, mark in self.marks[c_id].items():
                student_name = "Unknown"
                for s in self.students:
                    if s.get_id() == s_id:
                        student_name = s.get_name()
                        break
                print(f"Student: {student_name} (ID: {s_id}) - Mark: {mark}")
        else:
            print("No marks found for this course.")

    def run(self):
        self.input_students()
        self.input_courses()
        self.list_students()
        self.list_courses()
        for _ in range(len(self.courses)):
            self.input_marks()
        self.show_student_marks()

if __name__ == "__main__":
    manager = Management()
    manager.run()