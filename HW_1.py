class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg = sum(self.grades.values())/len(self.grades.values())

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Средний балл: {self.avg}, Курсы в процессе изучения: {self.courses_in_progress}, Завершенные курсы: {self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def rate(self):
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'


class Reviewer (Mentor):
    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


Ray = Reviewer('Ray', 'Ricky')
print(Ray)

Lui = Lecturer('Lui', 'Law')
print(Lui)

Sam = Student('Sam', 'Eman', 'male')
Sam.courses_in_progress += ['Python']

Ray = Reviewer('Ray', 'Ricky')
Ray.courses_attached += ['Python']

Ray.rate_hw(Sam, 'Python', 10)
Ray.rate_hw(Sam, 'Python', 10)
Ray.rate_hw(Sam, 'Python', 10)

print(Sam.grades)
print(Sam)