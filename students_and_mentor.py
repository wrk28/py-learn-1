class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, point):
        pass


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
       
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.points = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        pass

student1 = Student("Alex", "Johnson", "Male")
lecture1 = Lecturer("John", "Johnson")
reviewer1 = Reviewer("Peter", "Johnson")