class Student:
    def __init__(self, s_id, name, dob):
       self.id = s_id
       self.name = name
       self.dob = dob
       self.gpa = 0.0

class Course:
    def __init__(self, c_id, name, credits):
        self.id = c_id
        self.name = name
        self.credits = credits
