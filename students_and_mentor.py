class Student:
    def __init__(self, name, surname, gender):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__finished_courses = []
        self.__courses_in_progress = []
        self.__grades = {}

    def rate_lecturer(self, lecturer, course, point):
        if  set(self.__courses_in_progress) & lecturer.getCourses() and\
            point in range(0, 11):
            lecturer.receive_points(course, point)   
        else:
            print("Ошибка!")

    def receive_grade(self, course, grade):
        if course in self.__courses_in_progress:
            if course in self.__grades:
                self.__grades[course] += [grade]
            else:
                self.__grades[course] = [grade]
        else:
            print('Ошибка!')

    def __str__(self):
        return  f'Имя: {self.__name}\n'\
                f'Фамилия: {self.__surname}\n'\
                f'Средняя оценка за домашние задания: {1}\n'\
                f'Курсы в процессе изучения: {",".join(self.__courses_in_progress)}\n'\
                f'Завершенные курсы: {",".join(self.__finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._courses_attached = []
        
       
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.__points = {}

    def receive_points(self, course, point):
        if course in self._courses_attached:
            if course in self.__points:
                self.__points[course] += [point]
            else:
                self.__points[course] = [point]
        else:
            print("Ошибка!")

    def getCourses(self) -> set:
        return set(self._courses_attached)
    
    def __str__(self):
        return  f'Имя: {self._name}\n'\
                f'Фамилия: {self._surname}\n'\
                f'Средняя оценка за лекции: {1}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self._courses_attached:
            student.receive_grade(course, grade)
        else:
            print('Ошибка!')

    def __str__(self):
        return  f'Имя: {self._name}\n'\
                f'Фамилия: {self._surname}'


student1 = Student("Alex", "Johnson", "Male")
lecture1 = Lecturer("John", "Johnson")
reviewer1 = Reviewer("Peter", "Johnson")

print(student1)
print(lecture1)
print(reviewer1)