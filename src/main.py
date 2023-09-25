from registrar import Registrar


def main():
    # Create a Registrar instance
    registrar = Registrar()

    # Add some students
    registrar.add_student("S001", "Adam")
    registrar.add_student("S002", "Luis")
    registrar.add_student("S003", "Luis")

    # Add some courses
    registrar.add_course("C001", "Math 101", 9, 10)
    registrar.add_course("C002", "Physics 101", 10, 11)
    registrar.add_course("C003", "Chemistry 101", 1, 2)
    registrar.add_course("C004", "Intro to Computer Science", 4, 5)

    # Enroll Adam in Math 101
    registrar.enroll_student("S001", "C001")
    registrar.enroll_student("S001", "C003")
    registrar.enroll_student("S001", "C004")

    # Enroll Luis in Physics 101
    registrar.enroll_student("S002", "C002")

    # Print student schedules
    print("\nAdam's Schedule:")
    registrar.print_student_schedule("S001")

    print("\nLuis' Schedule:")
    registrar.print_student_schedule("S002")

    # Print course rosters
    print("\nMath 101 Roster:")
    registrar.print_course_roster("C001")

    print("\nPhysics 101 Roster:")
    registrar.print_course_roster("C002")

    print("\nChemistry 101 Roster:")
    registrar.print_course_roster("C003")

    registrar.print_course_roster("C004")

    # Add some courses
    registrar.add_course("C001", "Math 101", 9, 10)
    registrar.add_course("C002", "Physics 101", 10, 11)
    registrar.add_course("C003", "Chemistry 101", 1, 2)

    # Enroll Adam in Math 101 and Physics 101
    registrar.enroll_student("S001", "C001")
    registrar.enroll_student("S001", "C002")
    registrar.print_course_roster("C001")
    registrar.print_student_schedule("S001")


if __name__ == "__main__":
    main()
