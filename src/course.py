# Add a class that will represent the course
class Course:

    # Add a constructor that will intialize the course's name and id
    def __init__(self, course_name, course_id, start_time, end_time):
        self.course_name = course_name
        self.course_id = course_id
        self.start_time = start_time
        self.end_time = end_time
        self.students = set()

    def conflicts_with(self, other_course):
        return not (self.end_time <= other_course.start_time or self.start_time >= other_course.end_time)
