
# Add a class that will represent the student


class Student:

    # Add a constructor that will initialize the student's name and id
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = set()

# Add a class that will represent the course


class Course:

    # Add a constructor that will intialize the course's name and id
    def __init__(self, course_name, course_id, start_time, end_time):
        self.course_name = course_name
        self.course_id = course_id
        self.start_time = start_time
        self.end_time = end_time
        self.students = set()


# Add a class that will represent the registrar system


class Registrar:

    def __init__(self):
        self.courses = {}
        self.students = {}

    def add_course(self, course_id, course_name):
        if course_id not in self.courses:
            self.courses[course_id] = Course(course_name, course_id)
        else:
            print("Course already added.")

    def remove_course(self, course_id):
        if course_id in self.courses:
            del self.courses[course_id]
        else:
            print("Course does not exist")

    def add_student(self, student_id, student_name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_name, student_id)
        else:
            print("Student already added.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            print("Student does not exist")

    def enroll_student(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            self.students[student_id].courses.add(self.courses[course_id])
            self.courses[course_id].students.add(self.students[student_id])
        else:
            print("Student or course does not exist")

    def print_course_roster(self, course_id):
        if course_id in self.courses:
            for student in self.courses[course_id].students:
                print(student.student_name)
        else:
            print("Course does not exist")

    def print_student_schedule(self, student_id):
        if student_id in self.students:
            for course in self.students[student_id].courses:
                print(course.course_name)
        else:
            print("Student does not exist")


# Add a class that will represent the AVL tree and its methods


class Node:
    def __init__(self, course):
        self.course = course
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, root, course):
        if not root:
            return Node(course)
        if course.start_time < root.course.start_time:
            root.left = self.insert(root.left, course)
        elif course.start_time > root.course.start_time:
            root.right = self.insert(root.right, course)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and course < root.left.course:
            return self.right_rotate(root)
        if balance < -1 and course > root.right.course:
            return self.left_rotate(root)
        if balance > 1 and course > root.left.course:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and course < root.right.course:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.key, end=" ")
            self.in_order_traversal(node.right)


if __name__ == "__main__":
    tree = AVLTree()
    # Insert some keys into the tree
    tree.root = tree.insert(tree.root, 10)
    tree.root = tree.insert(tree.root, 20)
    tree.root = tree.insert(tree.root, 30)
    # Print the tree in-order
    tree.in_order_traversal(tree.root)
