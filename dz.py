class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def learning(self):
        learn = ''
        for k in self.courses_in_progress:
            learn += k + ', '
        return learn[:-2]

    def done(self):
        if len(self.finished_courses) != 0:
            for k in self.finished_courses:
                return k
        else:
            c = 'Ещё нет завершенных курсов'
            return c

    def st_average_grade(self):
        for i in self.grades:
            aver = 0
            num = 1
            n = 0
            for k in self.grades.get(i):
                k = self.grades.get(i)[n] / num
                num += 1
                n += 1
                return k
        # return i
    def __eq__(self, other):
        return (self.st_average_grade() == other.st_average_grade())

    def __ne__(self, other):
        return (self.st_average_grade() != other.st_average_grade())

    def __lt__(self, other):
        return (self.st_average_grade() < other.st_average_grade())

    def __gt__(self, other):
        return (self.st_average_grade() > other.st_average_grade())

    def __le__(self, other):
        return (self.st_average_grade() <= other.st_average_grade())

    def __ge__(self, other):
        return (self.st_average_grade() >= other.st_average_grade())

    def __str__(self):
        return (f"Имя: { self.name }\nФамилия: { self.surname }\nСредняя оценка за домашние задания: { self.st_average_grade() }\n"
                f"Курсы в процессе изучения: { self.learning() }\nЗавершенные курсы: { self.done() }\n")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def lec_average_grade(self):
        for i in self.grades:
            aver = 0
            num = 1
            n = 0
            for k in self.grades.get(i):
                k = self.grades.get(i)[n] / num
                num += 1
                n += 1
                return k

    def __eq__(self, other):
        return (self.lec_average_grade() == other.lec_average_grade())

    def __ne__(self, other):
        return (self.lec_average_grade() != other.lec_average_grade())

    def __lt__(self, other):
        return (self.lec_average_grade() < other.lec_average_grade())

    def __gt__(self, other):
        return (self.lec_average_grade() > other.lec_average_grade())

    def __le__(self, other):
        return (self.lec_average_grade() <= other.lec_average_grade())

    def __ge__(self, other):
        return (self.lec_average_grade() >= other.lec_average_grade())

    def __str__(self):
        return f"Имя: { self.name }\nФамилия: { self.surname }\nСредняя оценка за лекции: { self.lec_average_grade() }\n"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: { self.name }\nФамилия: { self.surname }\n"



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['CSS']

nbest_student = Student('Ruoy', 'Eman', 'your_gender')
nbest_student.courses_in_progress += ['Python']
nbest_student.courses_in_progress += ['CSS']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['CSS']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(nbest_student, 'Python', 6)
cool_mentor.rate_hw(nbest_student, 'Python', 7)
cool_mentor.rate_hw(nbest_student, 'Python', 10)

equality = best_student > nbest_student

lector = Lecturer('Name', 'Surname')
lector.courses_attached += ['Python']
best_student.rate_lec(lector, 'Python', 10)

print(best_student)
print(lector)
print(equality)
