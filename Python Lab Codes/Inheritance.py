class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_student_info(self):
        super().display_info()
        print("Student ID:", self.student_id)
        print("Course:", self.course)

student1 = Student("Toast", 19, "TOT33", "Computer Science")

student1.display_student_info()
