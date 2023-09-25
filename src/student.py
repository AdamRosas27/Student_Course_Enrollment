# Add a class that will represent the student
class Student:

    # Add a constructor that will initialize the student's name and id
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = set()
