""" Can use a hashmap to store the students names as a key and the list of classes their enrolled in as the value for easy lookup """

""" Can use an avl tree to represent all the courses available. For instance, "Courses" could be the root and each course would be children of the root "courses". and each child node could be a hashmap """


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
