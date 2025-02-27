class Student:
    def __init__(self, name, surname, gender):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__finished_courses = []
        self.__courses_in_progress = []
        self.__grades = {}

    def rate_lecturer(self, lecturer, course, point):
        pass

    def receive_grade(self, course, grade):
        if course in self.__courses_in_progress:
            if course in self.__grades:
                self.__grades[course] += [grade]
            else:
                self.__grades[course] = [grade]
        else:
            print('Ошибка!')


class Mentor:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self._courses_attached = []
        
       
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.__points = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self._courses_attached:
            student.receive_grade(course, grade)
        else:
            print('Ошибка!')
        


           

student1 = Student("Alex", "Johnson", "Male")
lecture1 = Lecturer("John", "Johnson")
reviewer1 = Reviewer("Peter", "Johnson")