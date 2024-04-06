class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if not self.grades:
            return 0
        grades_list_s = []
        for grade in self.grades.values():
            grades_list_s.extend(grade)
        return round(sum(grades_list_s) / len(grades_list_s), 2)

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')

    def __lt__(self, student2):
        if not isinstance(student2, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grade() < student2.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        grades_list_l = []
        for grade in self.grades.values():
            grades_list_l.extend(grade)
        return round(sum(grades_list_l) / len(grades_list_l), 2)

    def __lt__(self, lector2):
        if not isinstance(lector2, Lecturer):
            print('Не лектор!')
            return
        return self.average_grade() < lector2.average_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student1 = Student('Maksim', 'Mitrofanov', 'you_gender')
student2 = Student('Sergey', 'Serebrin', 'your_gender')

mentor1 = Mentor('Oleg', 'Vlasov')
mentor2 = Mentor('Ivan', 'Tarasov')

lector1 = Lecturer('Nikolay', 'Vozov')
lector2 = Lecturer('Ilya', 'Kolesov')

reviewer1 = Reviewer('Anton', 'Rogov')
reviewer2 = Reviewer('Victor', 'Barinov')

student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']

student1.finished_courses += ['Введение в программирование']

student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']

student2.finished_courses += ['Введение в программирование']

reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

lector1.courses_attached += ['Python']
lector1.courses_attached += ['Git']

lector2.courses_attached += ['Python']
lector2.courses_attached += ['Git']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)

reviewer1.rate_hw(student2, 'Python', 6)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 7)

reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 9)

reviewer2.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 7)

student1.rate_lw(lector1, 'Python', 10)
student1.rate_lw(lector1, 'Python', 9)
student1.rate_lw(lector1, 'Python', 10)

student1.rate_lw(lector2, 'Python', 10)
student1.rate_lw(lector2, 'Python', 8)
student1.rate_lw(lector2, 'Python', 9)

student2.rate_lw(lector1, 'Python', 10)
student2.rate_lw(lector1, 'Python', 10)
student2.rate_lw(lector1, 'Python', 10)

student2.rate_lw(lector2, 'Python', 10)
student2.rate_lw(lector2, 'Python', 9)
student2.rate_lw(lector2, 'Python', 9)

print(f'Student1:\n{student1}')
print(f'Student2:\n{student2}')
print(f'Lector1: \n{lector1}')
print(f'Lector2: \n{lector2}')
print(f'Reviewer1:\n{reviewer1}')
print(f'Reviewer2:\n{reviewer2}')


def average_grade_student(students, course):
    if not isinstance(students, list):
        return 'Not list'
    grades_list_s = []
    for student in students:
        if course in student.grades:
            grades_list_s.extend(student.grades[course])

        if not grades_list_s:
            return 'По такому курсу ни у кого нет оценок'

    return round(sum(grades_list_s) / len(grades_list_s), 2)


print(f'Средняя оценка всех студентов на курсе Python - {average_grade_student([student1, student2], "Python")}')


def average_grade_lecturer(lecturers, course):
    if not isinstance(lecturers, list):
        return 'Not list'
    grades_list_l = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades_list_l.extend(lecturer.grades[course])

        if not grades_list_l:
            return 'По такому курсу ни у кого нет оценок'

    return round(sum(grades_list_l) / len(grades_list_l), 2)


print(f'Средняя оценка всех лекторов на курсе Python - {average_grade_lecturer([lector1, lector2], "Python")}')
