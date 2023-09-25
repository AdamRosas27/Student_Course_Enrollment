from student import Student
from course import Course
from avl_tree import AVLTree


class Registrar:

    def __init__(self):
        self.courses = {}
        self.students = {}
        self.course_tree = AVLTree()

    def add_course(self, course_id, course_name, start_time, end_time):
        if course_id not in self.courses:
            new_course = Course(course_name, course_id, start_time, end_time)
            self.courses[course_id] = new_course
            self.course_tree.root = self.course_tree.insert(
                self.course_tree.root, new_course)
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
            student = self.students[student_id]
            course_to_enroll = self.courses[course_id]

            if self.course_conflicts(self.course_tree.root, course_to_enroll):
                print(
                    f"Cannot enroll in {course_to_enroll.course_name} due to time conflict.")
                return

            student.courses.add(course_to_enroll)
            course_to_enroll.students.add(student)

        else:
            print("Student or course does not exist")

    def print_course_roster(self, course_id):
        for students in self.courses[course_id].students:
            print(students.student_name)

    def print_student_schedule(self, student_id):
        for courses in self.students[student_id].courses:
            print(courses.course_name)

    def course_conflicts(self, root, course_to_check):
        if not root:
            return False
        if root.course.conflicts_with(course_to_check):
            return True
        if course_to_check.start_time < root.course.start_time:
            return self.course_conflicts(root.left, course_to_check)
        return self.course_conflicts(root.right, course_to_check)
