# Student Course Enrollment 

This project focuses on enhancing the university Registrar's Office system to efficiently manage student enrollment and course registration. The primary goal is to design and implement data structures, specifically HashMaps and AVL Trees, to facilitate tasks like enrollment, registration, roster generation, student schedule management, and conflict resolution. The project aims to create an effective and optimized system for streamlining these critical aspects of academic administration.

## Table of Contents

- [Student Course Enrollment](#student-course-enrollment)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Usage](#usage)
    - [Setup](#setup)
    - [Basic Functionalities](#basic-functionalities)
    - [Running Test](#running-test)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Introduction

The project revolves around improving the functionality of the university's Registrar's Office system. Its purpose is to streamline the management of student enrollment and course registration by implementing efficient data structures, namely HashMaps and AVL Trees. The primary goal is to design a system capable of handling key tasks such as enrollment, registration, roster generation, student schedule management, and conflict resolution. This initiative stems from the need to enhance the university's administrative processes, ensuring a more organized and efficient approach to student course enrollment and registration, ultimately benefiting both students and the institution.

## Features

- Student Enrollment: Students enroll in courses each semester. Each student has a unique student ID, and each course has a unique course code. Students can enroll in multiple courses, and courses can have multiple enrolled students.
- Course Registration: Students can add or drop courses during the registration period. The registration system should efficiently allow students to perform these actions.
- Course Roster: The university needs a way to generate a roster for each course, listing all the enrolled students.
- Student Schedule: Each student should be able to view their current schedule, which lists the courses they are enrolled in.
- Conflict Resolution: Ensure that students are not able to enroll in courses with overlapping schedules.

## Usage

### Setup

1. Ensure you have the files: student.py, course.py, registrar.py, and avl_tree.py.
2. Import the required classes:
```from registrar import Registrar```

### Basic Functionalities
1. Add Student:
```registrar = Registrar() registrar.add_student("S001", "Alice")```
2. Add Course:
```registrar.add_course("C001", "Math 101", 9, 10)  # 9 AM to 10 AM```
3. Enroll Student:
```registrar.enroll_student("S001", "C001")```
4. View Student Schedule:
```registrar.print_student_schedule("S001")```
5. View Course Roster
```registrar.print_course_roster("C001")```

### Running Test
```if __name__ == "__main__": main()```


## License

N/A

## Acknowledgments

- Adam Rosas
- Luis Silva
- Luis Romero
