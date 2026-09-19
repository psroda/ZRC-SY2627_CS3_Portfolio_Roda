class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


student1 = Student("Sofia", "2024-018")
student2 = Student("LaVyrly", "2024-012")

course = Course("Computer Science 3")

course.add_student(student1)
course.add_student(student2)

print("Course:", course.course_name)
print("Students:")

for student in course.students:
    print(student.name, "-", student.student_id)
