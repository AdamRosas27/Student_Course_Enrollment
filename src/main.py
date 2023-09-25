from registrar import Registrar
from avl_tree import AVLTree
from course import Course


def main():
    # Create a Registrar instance
    registrar = Registrar()

    # Add some students
    registrar.add_student("S001", "Alice")
    registrar.add_student("S002", "Bob")

    # Add some courses
    registrar.add_course("C001", "Math 101", 9, 10)
    registrar.add_course("C002", "Physics 101", 10, 11)

    # Enroll Alice in Math 101
    registrar.enroll_student("S001", "C001")

    # Enroll Bob in Physics 101
    registrar.enroll_student("S002", "C002")

    # Print student schedules
    print("\nAlice's Schedule:")
    registrar.print_student_schedule("S001")

    print("\nBob's Schedule:")
    registrar.print_student_schedule("S002")

    # Print course rosters
    print("\nMath 101 Roster:")
    registrar.print_course_roster("C001")

    print("\nPhysics 101 Roster:")
    registrar.print_course_roster("C002")

    print("\nChemistry 101 Roster:")
    registrar.print_course_roster("C003")

    # Add some courses
    registrar.add_course("C001", "Math 101", 9, 10)
    registrar.add_course("C002", "Physics 101", 10, 11)
    registrar.add_course("C003", "Chemistry 101", 11, 12)

    # Enroll Alice in Math 101 and Physics 101
    registrar.enroll_student("S001", "C001")
    registrar.enroll_student("S001", "C002")
    registrar.print_course_roster("C001")
    registrar.print_student_schedule("S001")


if __name__ == "__main__":
    main()
