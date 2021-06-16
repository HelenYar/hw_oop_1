class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


# добавляем оценку за лекцию Lecturer
    def rate_lecture(self, lecturer, course, grade_lect):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            lecturer.grades_lecturer += [grade_lect]
        else:
            return 'Ошибка'

# находим ср оценку студента за дз
    def st_avg_grade(self):
        count = 0
        sum_hw = 0
        for graders in self.grades.values():
            sum_hw += sum(graders)
            count += len(graders)
        return round(sum_hw / count, 2)

# сравниваем между собой лекторов по средней оценке за лекции
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not in Student')
            return
        else:
            compare = self.st_avg_grade() < other.st_avg_grade()
            if compare:
                print(f'У {self.name} {self.surname} ср. оценка ниже, чем у {other.name} {other.surname} ')
            else:
                print(f'У {other.name} {other.surname} ср. оценка ниже, чем у {self.name} {self.surname} ')
        return compare

    # Перегружаем магический метод __str__ для  Student
    def __str__(self):
        res = f'\n' \
              f'Student\n' \
              f'Имя: {self.name} \nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {  self.st_avg_grade() }  \n' \
              f'Курсы в процессе изучения:{self.courses_in_progress}\n' \
              f'Завершенные курсы:{self.finished_courses}\n' \
              f' '
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lecturer = []


# Перегружаем магический метод __str__ для  Lecturer

    def __str__(self):
        res = f'Lecturer\n' \
              f'Имя: {self.name} \nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: { round(sum(self.grades_lecturer)/len(self.grades_lecturer), 2) }\n' \
              f' '
        return res

# сравниваем между собой лекторов по средней оценке за лекции
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not in Lecturer')
            return
        else:
            compare = (sum(self.grades_lecturer)/len(self.grades_lecturer)) < \
               (sum(other.grades_lecturer)/len(other.grades_lecturer))
            if compare:
                print(f'У {self.name} {self.surname} ср. оценка ниже, чем у {other.name} {other.surname} ')
            else:
                print(f'У {other.name} {other.surname} ср. оценка ниже, чем у {self.name} {self.surname} ')
        return compare


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

# добавляем оценку за дз Student
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Перегружаем магический метод __str__ для  Reviewer
    def __str__(self):
        res = f'\n' \
              f'Reviewer\n' \
              f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res

# студенты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Java']

petrov_student = Student('Petty', 'Petrov', 'your_gender')
petrov_student.courses_in_progress += ['Python']
petrov_student.courses_in_progress += ['C++']
petrov_student.courses_in_progress += ['Java']

# проверяющие
cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']
cool_Reviewer.courses_attached += ['C++']

py_Reviewer = Reviewer('S', 'B')
py_Reviewer.courses_attached += ['Python']

# вызываеи ф-цию выставления оценки студенту за дз
cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 9)
cool_Reviewer.rate_hw(best_student, 'Python', 8)

py_Reviewer.rate_hw(petrov_student, 'Python', 6)
cool_Reviewer.rate_hw(petrov_student, 'C++', 10)
cool_Reviewer.rate_hw(petrov_student, 'C++', 8)

# лектора
good_lecturer = Lecturer('Ivan', 'Ivanov')
good_lecturer.courses_attached += ['Python']
good_lecturer.courses_attached += ['C++']

super_lecturer = Lecturer('Ivan', 'Petrov')
super_lecturer.courses_attached += ['Java']

# вызываеи ф-цию выставления оценки лектору за лекцию
petrov_student.rate_lecture(good_lecturer, 'Python', 10)
petrov_student.rate_lecture(good_lecturer, 'C++', 8)
best_student.rate_lecture(good_lecturer, 'Python', 8)

petrov_student.rate_lecture(super_lecturer, 'Java', 10)
petrov_student.rate_lecture(super_lecturer, 'Java', 6)

# выводим перегруженный метод  __str__
print(good_lecturer)
print(super_lecturer)
print(good_lecturer < super_lecturer)  # сравниваем лекторов по средней оценке за лекции

print(best_student)
print(petrov_student)
print(petrov_student < best_student)  # сравниваем студентов по средней оценке за дз

print(cool_Reviewer)
print(py_Reviewer)


def st_avg_grade_hw(student_list, course):
    sum_all = 0
    for student in student_list:
        for cr, grades in student.grades.items():
            if cr == course:
                sum_all += sum(grades) / len(grades)
    return round(sum_all / len(student_list), 2)


print(st_avg_grade_hw([best_student, petrov_student], 'Python'))


def lect_avg_grade(lect_list):
    sum_all = 0
    for lecturer in lect_list:
        sum_all += sum(lecturer.grades_lecturer) / len(lecturer.grades_lecturer)
    return round(sum_all / len(lect_list), 2)


print(lect_avg_grade([good_lecturer, super_lecturer]))

# выводим оценки студента за дз
# (best_student.grades)
# print(petrov_student.grades)

# выводим оценки лектора за лекции
# print(good_lecturer.grades_lecturer)
# print(super_lecturer.grades_lecturer)
