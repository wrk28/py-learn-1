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

    def __avg_grade(self):
        grades = 0
        number = 0  
        for course in self.__grades:
            grades += sum(course.values())
            number += len(course.values())
        return grades/number if number != 0 else 0


    def __str__(self):
        return  f'Имя: {self.__name}\n'\
                f'Фамилия: {self.__surname}\n'\
                f'Средняя оценка за домашние задания: {self.__avg_grade()}\n'\
                f'Курсы в процессе изучения: {",".join(self.__courses_in_progress)}\n'\
                f'Завершенные курсы: {",".join(self.__finished_courses)}'

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.__avg_grade() == student.__avg_grade()
        else:
            return None
    
    def __ne__(self, student):
        if isinstance(student, Student):
            return self.__avg_grade() != student.__avg_grade()
        else:
            return None
        
    def __gt__(self, student):
        if isinstance(student, Student):
            return self.__avg_grade() > student.__avg_grade()
        else:
            return None
    
    def __ge__(self, student):
        if isinstance(student, Student):
            return self.__avg_grade() >= student.__avg_grade()
        else:
            return None
        
    def __lt__(self, student):
        if isinstance(student, Student):
            return self.__avg_grade() < student.__avg_grade()
        else:
            return None
        
    def __le__(self, student):
        if isinstance(student, Student):
            return self.__avg_grade() <= student.__avg_grade()
        else:
            return None
    
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
    
    def __avg_point(self):
        points = 0
        number = 0  
        for course in self.__points:
            points += sum(course.values())
            number += len(course.values())
        return points/number if number != 0 else 0
    
    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.__avg_point() == lecturer.__avg_point()
        else:
            return None
          
    def __ne__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.__avg_point() != lecturer.__avg_point()
        else:
            return None
            
    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.__avg_point() > lecturer.__avg_point()
        else:
            return None
            
    def __ge__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.__avg_point() >= lecturer.__avg_point()
        else:
            return None
                
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.__avg_point() < lecturer.__avg_point()
        else:
            return None
                
    def __le__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.__avg_point() <= lecturer.__avg_point()
        else:
            return None
                
    def __str__(self):
        return  f'Имя: {self._name}\n'\
                f'Фамилия: {self._surname}\n'\
                f'Средняя оценка за лекции: {self.__avg_point()}'


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
student2 = Student("Alexa", "Johnson", "Female")
lecture1 = Lecturer("John", "Johnson")
reviewer1 = Reviewer("Peter", "Johnson")

print(student1 > student2)
print(lecture1)
print(reviewer1)