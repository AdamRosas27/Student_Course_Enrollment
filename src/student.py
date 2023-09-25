# Add a class that will represent the student
class Student:

    # Add a constructor that will initialize the student's name and id
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = set()

    def print_schedule(self, student_id):
        if student_id in self.students:
            for course in self.students[student_id].courses:
                print(course.course_name)
