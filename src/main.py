# Import collections to be able to use the set data structure
from collections import set as Set

# Add a class that will represent the student


class Student:

    # Add a constructor that will initialize the student's name and id
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = Set()

# Add a class that will represent the course


class Course:

    # Add a constructor that will intialize the course's name and id
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.students = Set()


# Add a class that will represent the registrar system


class Registrar:
    pass

# Add a class that will represent the AVL tree and its methods


class AVLTree:
    pass

# Add a class that will represent the nodes of the AVL tree


class AVLNode:
    pass
