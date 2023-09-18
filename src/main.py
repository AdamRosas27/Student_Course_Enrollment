""" Can use a hashmap to store the students names as a key and the list of classes their enrolled in as the value for easy lookup """


class Courses:

    def __init__(self, course, student):
        self.course = course
        self.student = student

    # Create a method that returns the roster of the course which returns a list of students enrolled in the course


class Student:

    def __init__(self, ID, courses=[]):
        self.ID = ID
        self.courses = courses

    # Create a method that adds a course to a students class list

    # Create a method that removes a course from a students class list

    # Create a method that allows the student to view their current course schedules
