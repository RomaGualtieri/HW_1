class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_rate(self):
        global average_rate
        sum_rate = 0
        len_rate = 0
        for course in self.grades.values():
            sum_rate += sum(course)
            len_rate += len(course)
            average_rate = round(sum_rate / len_rate, 2)
        return average_rate

    def avg_rate_course(self, course):
        sum_rate = 0
        len_rate = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rate += sum(self.grades[course])
                len_rate += len(self.grades[course])
        average_rate = round(sum_rate / len_rate, 2)
        return average_rate

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнивать можно только студентов')
            return
        return self.avg_rate() < other.avg_rate()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за дз: {self.avg_rate()}\nКурсы в ' \
               f'процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: ' \
               f'{", ".join(self.finished_courses)} '


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_rate(self):
        global average_rate
        sum_rate = 0
        len_rate = 0
        for rate in self.grades.values():
            sum_rate += sum(rate)
            len_rate += len(rate)
            average_rate = round(sum_rate / len_rate, 2)
        return average_rate

    def avg_rate_course(self, course):
        sum_rate = 0
        len_rate = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rate += sum(self.grades[course])
                len_rate += len(self.grades[course])
        average_rate = round(sum_rate / len_rate, 2)
        return average_rate

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнивать можно только лекторов')
            return
        return self.avg_rate() < other.avg_rate()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


Student_1 = Student('Roma', 'Kvit', 'male')
Student_2 = Student('Ivan', 'Ivanov', 'male')

Rev_1 = Reviewer('R', 'Big')
Rev_2 = Reviewer('R', 'Lit')

Lec_1 = Lecturer('L', 'Big')
Lec_2 = Lecturer('L', 'Lit')

Student_1.courses_in_progress += ['Python', 'Git']
Student_1.finished_courses += ['Введение в программирование']
Student_2.courses_in_progress += ['Python', 'Git']
Student_2.finished_courses += ['Введение в программирование']

Rev_1.courses_attached += ['Python', 'Git']
Rev_2.courses_attached += ['Python', 'Git']
Lec_1.courses_attached += ['Python', 'Git']
Lec_2.courses_attached += ['Python', 'Git']

Student_1.rate_lecturer(Lec_1, 'Python', 9)
Student_1.rate_lecturer(Lec_1, 'Python', 7)
Student_1.rate_lecturer(Lec_1, 'Python', 8)

Student_1.rate_lecturer(Lec_1, 'Git', 2)
Student_1.rate_lecturer(Lec_1, 'Git', 2)
Student_1.rate_lecturer(Lec_1, 'Git', 2)

Student_1.rate_lecturer(Lec_2, 'Python', 2)
Student_1.rate_lecturer(Lec_2, 'Python', 4)
Student_1.rate_lecturer(Lec_2, 'Python', 3)

Student_1.rate_lecturer(Lec_2, 'Git', 10)
Student_1.rate_lecturer(Lec_2, 'Git', 10)
Student_1.rate_lecturer(Lec_2, 'Git', 10)

Student_2.rate_lecturer(Lec_1, 'Python', 10)
Student_2.rate_lecturer(Lec_1, 'Python', 9)
Student_2.rate_lecturer(Lec_1, 'Python', 10)

Student_2.rate_lecturer(Lec_1, 'Git', 2)
Student_2.rate_lecturer(Lec_1, 'Git', 2)
Student_2.rate_lecturer(Lec_1, 'Git', 1)

Student_2.rate_lecturer(Lec_2, 'Python', 1)
Student_2.rate_lecturer(Lec_2, 'Python', 5)
Student_2.rate_lecturer(Lec_2, 'Python', 2)

Student_2.rate_lecturer(Lec_2, 'Git', 10)
Student_2.rate_lecturer(Lec_2, 'Git', 10)
Student_2.rate_lecturer(Lec_2, 'Git', 10)

Rev_1.rate_hw(Student_1, 'Python', 10)
Rev_1.rate_hw(Student_1, 'Python', 9)
Rev_1.rate_hw(Student_1, 'Python', 7)

Rev_1.rate_hw(Student_1, 'Git', 10)
Rev_1.rate_hw(Student_1, 'Git', 10)
Rev_1.rate_hw(Student_1, 'Git', 10)

Rev_1.rate_hw(Student_2, 'Python', 2)
Rev_1.rate_hw(Student_2, 'Python', 3)
Rev_1.rate_hw(Student_2, 'Python', 5)

Rev_1.rate_hw(Student_2, 'Git', 1)
Rev_1.rate_hw(Student_2, 'Git', 1)
Rev_1.rate_hw(Student_2, 'Git', 1)

Rev_2.rate_hw(Student_1, 'Python', 8)
Rev_2.rate_hw(Student_1, 'Python', 10)
Rev_2.rate_hw(Student_1, 'Python', 9)

Rev_2.rate_hw(Student_1, 'Git', 10)
Rev_2.rate_hw(Student_1, 'Git', 10)
Rev_2.rate_hw(Student_1, 'Git', 10)

Rev_2.rate_hw(Student_2, 'Python', 4)
Rev_2.rate_hw(Student_2, 'Python', 8)
Rev_2.rate_hw(Student_2, 'Python', 2)

Rev_2.rate_hw(Student_2, 'Git', 2)
Rev_2.rate_hw(Student_2, 'Git', 1)
Rev_2.rate_hw(Student_2, 'Git', 1)

student_list = [Student_1, Student_2]
lecturer_list = [Lec_1, Lec_2]


def avg_rate_all_man_course(list, course):
    sum_rate = 0
    len_rate = 0
    for man in list:
        sum_rate += man.avg_rate_course(course)
        len_rate += 1
    all_avg_rate = round(sum_rate / len_rate, 2)
    return all_avg_rate


# Задание 2
print(Student_1.grades)
print(Student_2.grades)
print(Lec_1.grades)
print(Lec_2.grades)

# Задание 3.1
print(Student_1)
print(Student_2)
print(Lec_1)
print(Lec_2)
# Задание 3.2
print(Student_1 > Student_2)
print(Lec_1 > Lec_2)

# Задание 4
print(avg_rate_all_man_course(student_list, 'Python'))
print(avg_rate_all_man_course(student_list, 'Git'))
print(avg_rate_all_man_course(lecturer_list, 'Python'))
print(avg_rate_all_man_course(lecturer_list, 'Git'))
