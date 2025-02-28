class Student:
    def __init__(self, name, surname, gender):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__finished_courses = []
        self.__courses_in_progress = []
        self.__grades = {}

    def rate_lecturer(self, lecturer, course, point):
        if  set(self.__courses_in_progress) & lecturer.get_course_list() and\
            point in range(0, 11):
            lecturer.receive_points(course, point)   
        else:
            print("Ошибка!")

    def get_full_name(self):
        return f'{self.__name} {self.__surname}'

    def receive_grade(self, course, grade):
        if course in self.__courses_in_progress:
            if course in self.__grades:
                self.__grades[course] += [grade]
            # now the course is added by take_course method
            # else:
            #   self.__grades[course] = [grade]
        else:
            print('Ошибка!')

    def take_course(self, course):
        if  course not in self.__courses_in_progress and \
            course not in self.__finished_courses:
            self.__courses_in_progress.append(course)
            self.__grades[course] = []
        else:
            print("Ошибка!")

    def avg_grade(self, course=None):
        if course is None:
            courses = self.__grades.items()
            grade_sum = sum(list(map(lambda course: sum(course[1]), courses)))
            grade_count = sum(list(map(lambda course: len(course[1]), courses)))
            return grade_sum/grade_count if grade_count > 0 else 0
        elif course in self.__grades:
            return sum(self.__grades[course]) / len(self.__grades[course]) \
                if len(self.__grades[course]) > 0 else 0
        else:
            return 0
    
    def end_course(self, course):
        if  course in self.__courses_in_progress and \
            course not in self.__finished_courses:
            self.__courses_in_progress.remove(course)
            self.__finished_courses.append(course)


    def __str__(self):
        return  f'Имя: {self.__name}\n'\
                f'Фамилия: {self.__surname}\n'\
                f'Средняя оценка за домашние задания: {self.avg_grade()}\n'\
                f'Курсы в процессе изучения: {", ".join(self.__courses_in_progress)}\n'\
                f'Завершенные курсы: {", ".join(self.__finished_courses)}'

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.avg_grade() == student.avg_grade()
        else:
            return None
    
    def __ne__(self, student):
        if isinstance(student, Student):
            return self.avg_grade() != student.avg_grade()
        else:
            return None
        
    def __gt__(self, student):
        if isinstance(student, Student):
            return self.avg_grade() > student.avg_grade()
        else:
            return None
    
    def __ge__(self, student):
        if isinstance(student, Student):
            return self.avg_grade() >= student.avg_grade()
        else:
            return None
        
    def __lt__(self, student):
        if isinstance(student, Student):
            return self.avg_grade() < student.avg_grade()
        else:
            return None
        
    def __le__(self, student):
        if isinstance(student, Student):
            return self.avg_grade() <= student.avg_grade()
        else:
            return None
    
class Mentor:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._courses_attached = []

    def get_full_name(self):
        return f'{self._name} {self._surname}'

    def assigned_for_course(self, course):
        if  course not in self._courses_attached and \
            course not in self._courses_attached:
            self._courses_attached.append(course)
        else:
            print("Ошибка!")
       
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.__points = {}

    def receive_points(self, course, point):
        if course in self._courses_attached:
            if course in self.__points.keys():
                self.__points[course] += [point]
            else:
                self.__points[course] = [point]
        else:
            print("Ошибка!")

    def get_course_list(self):
        return set(self._courses_attached)
    
    def avg_point(self, course=None):
        if course is None:
            courses = self.__points.items()
            point_sum = sum(list(map(lambda course: sum(course[1]), courses)))
            point_count = sum(list(map(lambda course: len(course[1]), courses)))
            return point_sum/point_count if point_count > 0 else 0
        elif course in self.__points:
            return sum(self.__points[course]) / len(self.__points[course]) \
                if len(self.__points[course]) > 0 else 0
        else:
            return 0

    
    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_point() == lecturer.avg_point()
        else:
            return None
          
    def __ne__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_point() != lecturer.avg_point()
        else:
            return None
            
    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_point() > lecturer.avg_point()
        else:
            return None
            
    def __ge__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_point() >= lecturer.avg_point()
        else:
            return None
                
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_point() < lecturer.avg_point()
        else:
            return None
                
    def __le__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_point() <= lecturer.avg_point()
        else:
            return None
                
    def __str__(self):
        return  f'Имя: {self._name}\n'\
                f'Фамилия: {self._surname}\n'\
                f'Средняя оценка за лекции: {self.avg_point()}'


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
    
def average_grade_dict(students: Student, course):
    grade_list = {}
    for student in students:
        grade_list[student.get_full_name()] = student.avg_grade(course)
    return str(grade_list)


def average_grade_total(students, course):
    adding = 0
    len = 0
    for student in students:
        adding += student.avg_grade(course)
        len += 1
    return adding/len if len !=0 else None

def average_point_dict(lectures, course):
    point_list = {}
    for lecture in lectures:
        point_list[lecture.get_full_name()] = lecture.avg_point(course)
    return str(point_list)

def average_point_total(lectures, course):
    adding = 0
    len = 0
    for lecture in lectures:
        adding += lecture.avg_point(course)
        len += 1
    return adding/len if len !=0 else None

def test():
    student1 = Student("Олег", "Естафьев", "Муж.")
    student1.take_course('физика')
    student1.take_course('математика')

    student2 = Student("Алёна", "Сергеевна", "Жен.")
    student2.take_course('физика')
    student2.take_course('математика')

    lecture1 = Lecturer("Борис", "Воскресенский")
    lecture1.assigned_for_course('математика')
    lecture1.assigned_for_course('физика')

    lecture2 = Lecturer("Антон", "Бережный")
    lecture2.assigned_for_course('физика')

    reviewer1 = Reviewer("Пётр", "Алексеев")
    reviewer1.assigned_for_course('физика')

    reviewer2 = Reviewer("Роман", "Антонов")
    reviewer2.assigned_for_course('математика')

    reviewer1.rate_hw(student1, 'физика', 8)
    reviewer1.rate_hw(student1, 'физика', 7)
    reviewer1.rate_hw(student2, 'физика', 7)
    reviewer1.rate_hw(student2, 'физика', 9)

    reviewer2.rate_hw(student1, 'математика', 7)
    reviewer2.rate_hw(student1, 'математика', 8)
    reviewer2.rate_hw(student2, 'математика', 9)
    reviewer2.rate_hw(student2, 'математика', 8)

    student1.rate_lecturer(lecture1, 'математика', 6)
    student1.rate_lecturer(lecture1, 'математика', 7)
    student1.rate_lecturer(lecture1, 'физика', 6)
    student1.rate_lecturer(lecture1, 'физика', 7)
    student1.rate_lecturer(lecture2, 'физика', 8)
    student1.rate_lecturer(lecture2, 'физика', 8)

    student2.rate_lecturer(lecture1, 'математика', 6)
    student2.rate_lecturer(lecture1, 'математика', 7)
    student2.rate_lecturer(lecture2, 'физика', 8)
    student2.rate_lecturer(lecture2, 'физика', 8)
    student2.rate_lecturer(lecture1, 'физика', 6)
    student2.rate_lecturer(lecture1, 'физика', 7)

    student1.end_course('физика')
    student2.end_course('математика')

    print(student1)
    print()
    print(student2)
    print()
    print(lecture1)
    print()
    print(lecture2)
    print()
    print(reviewer1)
    print()
    print(reviewer2)
    print()

    print(student1 == student2)
    print(student1 != student2)
    print(student1 >= student2)
    print(student1 <= student2)
    print(student1 > student2)
    print(student1 < student2)
    print()
    print(lecture1 == lecture2)
    print(lecture1 != lecture2)
    print(lecture1 >= lecture2)
    print(lecture1 <= lecture2)
    print(lecture1 > lecture2)
    print(lecture1 < lecture2)
    print()

    student_list = [student1, student2]
    lecture_list = [lecture1, lecture2]
    course = 'физика'

    print(f'Средняя оценка студентов по курсу {course}:',
          f'{average_grade_dict(student_list, course)}')
    print(f'Общая средняя оценка по курсу {course}:',
          f'{average_grade_total(student_list, course)}')
    print()
    print(f'Средняя оценка от студентов по лекциям {course}:',
          f'{average_point_dict(lecture_list, course)}')
    print(f'Общая средняя оценка от студентов по лекциям {course}:',
          f'{average_point_total(lecture_list, course)}')

if __name__ == '__main__':
    test()