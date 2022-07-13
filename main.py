class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        student_name = some_student.name
        student_surname = some_student.surname
        student_courses_in_progress = some_student.courses_in_progress
        student_finished_courses = some_student.finished_courses
        student_grades_list = []
        for key, value in self.grades.items():
            for grade in value:
                student_grades_list.append(grade)
        average_rating = sum(student_grades_list) / len(student_grades_list)
        return f'Имя: {student_name} \nФамилия: {student_surname}\nСредняя оценка за домашние задания: {average_rating}\nКурсы в процессе изучения: {student_courses_in_progress}\nЗавершенные курсы: {student_finished_courses}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}
    average_rating = float()

    def __str__(self):
        lecturer_name = some_lecturer.name
        lecturer_surname = some_lecturer.surname
        lecturer_grades_list = []
        for key, value in self.grades.items():
            for grade in value:
                lecturer_grades_list.append(grade)
        average_rating = sum(lecturer_grades_list) / len(lecturer_grades_list)
        return f'Имя: {lecturer_name}\nФамилия: {lecturer_surname}\nСредняя оценка за лекции: {average_rating}'

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Not a Mentor!')
            return
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_name = some_reviewer.name
        reviewer_surname = some_reviewer.surname
        return f'Имя: {reviewer_name} \nФамилия: {reviewer_surname}'

some_student = Student('Иван', 'Сидоров', 'male')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']

another_student = Student('Анна', 'Петрова', 'female')
another_student.courses_in_progress += ['Python']

some_lecturer = Lecturer('Екатерина', 'Тимофеева')
some_lecturer.courses_attached += ['Python']

another_lecturer = Lecturer('Илья', 'Орехов')
another_lecturer.courses_attached += ['Python']

some_student.rate_lecture(some_lecturer, 'Python', 8)
some_student.rate_lecture(some_lecturer, 'Python', 10)

some_student.rate_lecture(another_lecturer, 'Python', 8)

some_reviewer = Reviewer('Антон', 'Егоров')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_reviewer.rate_hw(another_student, 'Python', 10)
some_reviewer.rate_hw(another_student, 'Python', 8)
some_reviewer.rate_hw(another_student, 'Python', 10)

students = [some_student, another_student]
lecturers = [some_lecturer, another_lecturer]

def all_students(students):
    total_grade = []
    for student in students:
        for key, value in student.grades.items():
            if key == 'Python':
                for grade in value:
                    total_grade.append(grade)
    average_grades = sum(total_grade) / len(total_grade)
    print(f'Средняя оценка за домашние задания по курсу "Python": {average_grades}')

def all_lecturers(lecturers):
    total_grade = []
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == 'Python':
                for grade in value:
                    total_grade.append(grade)
    average_grades = sum(total_grade) / len(total_grade)
    print(f'Средняя оценка за лекции по курсу "Python": {average_grades}')


print(some_reviewer)
print(some_lecturer)
print(some_student)

print(some_lecturer.average_rating < another_lecturer.average_rating)
print(some_student.average_rating < another_student.average_rating)

all_students(students)
all_lecturers(lecturers)