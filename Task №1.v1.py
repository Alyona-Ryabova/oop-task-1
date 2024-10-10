class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

#Функция выставления оценок лекторам от студентов
    def grade_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.course_grades:
                    lecturer.course_grades[course] += [grade]
                else:
                    lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'
#Функция расчета средней оценки студентов
    def average_grade_st(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum/grades_count
        else:
            return 0
#Сравнение средних оценок студентов через операторов сравнения
    def __It__(self, other):
        if not isinstance(other, Student):
            return self.average_grade_st()<other.average_grade_st()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return self.average_grade_st() > other.average_grade_st()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return self.average_grade_st() == other.average_grade_st()

#Вывод данных студента
    def __str__(self):
        average = self.average_grade_st()
        some_student = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {round(average)}\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n 'f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return some_student

#Классы преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}
        Lecturer.lecturer_list.append(self)

# Функция расчета средней оценки лекторов
    def average_lecture_grade(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.course_grades:
            grades_count += len(self.course_grades[grade])
            grades_sum += sum(self.course_grades[grade])
        if grades_count > 0:
            return grades_sum/grades_count
        else:
            return 0

# Сравнение средних оценок лекторов через операторов сравнения
    def __It__(self, other):
        if not isinstance(other, Lecturer):
        return self.average_lecture_grade() < other.average_lecture_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
        return self.average_lecture_grade() > average_lecture_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
        return self.average_lecture_grade() == other.average_lecture_grade()

    # Вывод данных лектора
    def __str__(self):
        mean_grade = self.average_lecture_grade()
        some_lecturer = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {round(mean_grade)}\n'
        return some_lecturer

#Проверяющий, функция выставления оценок
class Reviewer(Mentor):
     def rate_hw(self, student, course, grade):
         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
         else:
            return 'Ошибка'
# Вывод данных проверяющего
    def __str__(self):
        some_reviewer = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'
        return some_reviewer


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)