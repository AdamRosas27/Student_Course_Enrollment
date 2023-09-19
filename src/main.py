class Courses:

    def __init__(self, course_name, course_id, schedule):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []
        self.schedule = schedule

    def add_student(self, student_id):
        pass

    def drop_student(self, student_id):
        pass

    def view_roster(self):
        pass


class Student:

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.enrolled_courses = set()

    def add_course(self, course_id):
        pass

    def drop_course(self, course_id):
        pass

    def view_schedule(self):
        pass


class Registration:

    def __init__(self):

        self.students = {}

    # Create a method that adds a course to a students class list
    def add_course(self, student_id, course_id):
        if student_id not in self.students and course_id in Courses:
            self.students[student_id] = course_id
            self.students.enroll

    # Create a method that removes a course from a students class list

    def drop_course(self, student_id, course_id):
        pass

    # Create a method that allows the student to view their current course schedules
    def view_schedule(self):
        pass

    # Create a method that returns the roster of the course which returns a list of students enrolled in the course
    def course_roster(self):
        pass
