class Courses:

    def __init__(self, course_name, course_id, schedule):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []
        self.schedule = schedule

    # Create a method that returns the roster of the course which returns a list of students enrolled in the course


class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.enrolled_courses = set()

    # Create a method that adds a course to a students class list

    # Create a method that removes a course from a students class list

    # Create a method that allows the student to view their current course schedules


class Registration:

    def __init__(self):

        self.students = {}
