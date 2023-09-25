# Questions 

## 1. Data Structure Design:
- A HashMap can be used to store student information due to its quick lookup. The key for the hashmap can be the students unique id number and the values can be other student information such as enrolled courses. Furthermore, An AVL tree can be utilized to resolve any scheduling conflicts within class times.

## 2. Enrollment Process:
- Each student would be uniquely identified because each student will have a unique student id number that corresponds with their name and their course information. Once a student is added to the course then the student will also be added to the course roster and the counrse will be added to the students schedule. 

## 3. Registration Process:
- Similar to the enrollment process, students can drop courses. This can be as simple as adding or removing the course from the dictionary (hashmap) or the set. You can remove a student from a course roster and the course will also be removed from the student schedule.

## 4. Generating Rosters: 
- Given the course code, the roster would be simply printing out all enrolled students within that course. Given the course id or course code, a for loop will print out all the values within the course set, in this case the values will be the enrolled students

## 5. Student Schedules:
- Similar to the roster generation, each students course schedule will be stored along their student id number within a set. A for loop will loop through the values within the set printing each values, in this case each value within the set will be a course.

## 6. Conflict Resolution:
- To ensure there is conflict resolution, this is in part of what the AVL tree will be used for. Each course will have a start and end time and the program will check if multiple courses have the same start and end times or if any of the class times overlap. If they do overlap, an error message will be printed out. 

## 7. Efficiency Considerations:
- Enrolling a student should take O(1) time complexity as we are simply adding a student to the set. As for generating a roster it would take approximately O(n) time complexity due to the for loop looping through each element in the set. This would be the same for checking a student's schedule. 