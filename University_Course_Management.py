from abc import ABC, abstractmethod
from Banking_System import Customer
from Validator_descriptors import Date


class Course(ABC):
    def __init__(self, name: str, instructor: str, content: str, credit: float or int):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.credit = credit
        self.__assignments = []

    @property
    def assignments(self):
        return self.__assignments

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Name must be of type int.')
        self.__name = value

    @property
    def instructor(self):
        return self.__instructor

    @instructor.setter
    def instructor(self, value):
        if not isinstance(value, str):
            raise ValueError('Please provide the name of the instructor as a str.')
        self.__instructor = value

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise ValueError('Content must be of type str.')
        self.__content = value

    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError('Credit must be of type int or float.')
        self.__credit = value

    def __repr__(self):
        return f'{self.name}'


class UndergraduateCourse(Course):
    def __init__(self, name, instructor, content, credit):
        super().__init__(name, instructor, content, credit)


class GraduateCourse(Course):
    def __init__(self, name, instructor, content, credit):
        super().__init__(name, instructor, content, credit)


class Assignment(ABC):
    deadline = Date('deadline')

    def __init__(self, name, content: str, deadline: str, student):
        self.deadline = deadline
        self.__content = content
        self.__name = name
        self.__student = student

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def name(self):
        return self.__name

    @property
    def student(self):
        return self.__student

    def __repr__(self):
        return f'{self.name}'


class Test(Assignment):
    def __init__(self, name, content, deadline, student):
        super().__init__(name, content, deadline, student)


class Essay(Assignment):
    def __init__(self, name, content, deadline, student):
        super().__init__(name, content, deadline, student)


class Dictation(Assignment):
    def __init__(self, name, content, deadline, student):
        super().__init__(name, content, deadline, student)


class Student(Customer):
    def __init__(self, name, email, phone_num):
        super().__init__(name, email, phone_num)
        self.__assignments = []
        self.__finished = []
        self.__handed_in = []
        self.__grades = {}

    @property
    def assignments(self):
        return self.__assignments

    @property
    def finished(self):
        return self.__finished

    @property
    def handed_in(self):
        return self.__handed_in

    @property
    def grades(self):
        return self.__grades

    def do_assignment(self, course: Course, assignment: Assignment):
        print(f'I\'m doing the {assignment} assignment for my {course} course')
        self.__finished.append(assignment.name)
        self.__assignments.remove(assignment.name)

    def hand_in_assignment(self, course: Course, assignment: Assignment):
        print(f'I handed in my {assignment} assignment for my {course} course.')
        self.__handed_in.append(assignment.name)

    def __repr__(self):
        return f'{self.name}'


class Professor(Customer):
    def __init__(self, name, email, phone_num):
        super().__init__(name, email, phone_num)
        self.__courses = []
        self.__assigned = {}
        self.__graded = {}

    @property
    def courses(self):
        return self.__courses

    @property
    def assigned(self):
        return self.__assigned

    @property
    def graded(self):
        return self.__graded

    def create_course(self, name, instructor, content, credit):
        course = Course(name, instructor, content, credit)
        self.__courses.append(course)

    @staticmethod
    def edit_course_name(course: Course, new_name):
        course.name = new_name

    @staticmethod
    def edit_course_instructor(course: Course, new_instructor):
        course.instructor = new_instructor

    @staticmethod
    def edit_course_content(course: Course, new_content):
        course.content = new_content

    def assign_homework(self, course: Course, name, content: str, deadline: str, student: Student):
        new_assignment = Assignment(name, content, deadline, student)
        course.assignments.append(new_assignment.name)
        if student.name in self.assigned:
            self.assigned[student.name].append(new_assignment.name)
        else:
            self.assigned[student.name] = [new_assignment.name]
        student.assignments.append(new_assignment.name)
        return new_assignment

    def grade_assignment(self, student: Student, assignment: Assignment, grade: int):
        if assignment.name not in self.graded:
            self.graded[assignment.name] = grade
            student.grades[assignment.name] = grade
            print(f'The has graded the assignment {grade} points.')
        else:
            print('Assignment already graded')

    def __repr__(self):
        return f'{self.name}'


if __name__ == '__main__':
    print('___________________________________________________________________________')
    print('Creating courses.')

    writing_skills = UndergraduateCourse('Writing Skills', 'Monica Geller', 'Chinese writing skills class', 20)
    reading_skills = GraduateCourse('Reading Skills', 'Ross Geller', 'Chinese reading skills class.', 10)

    print(writing_skills)
    print(reading_skills)

    print('___________________________________________________________________________')
    print('Creating professors.')

    monica = Professor('Monica Geller', 'monica.geller@gmail.com', '+37455676787')
    ross = Professor('Ross Geller', 'ross.geller@gmail.com', '+37433897845')

    print(monica)
    print(ross)

    print('___________________________________________________________________________')
    print('Creating students.')

    phoebe = Student('Phoebe Buffay', 'phoebe_buffay@gmail.com', '+37456729834')
    chandler = Student('Chandler Bing', 'chandler.bing@hotmail.com', '+37444675860')

    print(phoebe)
    print(chandler)

    print('___________________________________________________________________________')
    print('Getting info about the courses.')

    print(writing_skills.name)
    print(writing_skills.content)
    print(writing_skills.instructor)
    print(writing_skills.credit)

    print('___________________________________________________________________________')

    print(reading_skills.name)
    print(reading_skills.content)
    print(reading_skills.instructor)
    print(reading_skills.credit)

    print('___________________________________________________________________________')
    print('Getting info about the professors.')

    print(monica.name)
    print(monica.email)
    print(monica.phone_num)

    print('___________________________________________________________________________')

    print(ross.name)
    print(ross.email)
    print(ross.phone_num)

    print('___________________________________________________________________________')
    print('Assigning homework.')

    essay = monica.assign_homework(writing_skills, 'essay', 'Write an essay.', '03.01.2024', phoebe)
    print('Assignment: ', essay)
    print('Deadline: ', essay.deadline)
    print('Student', essay.student)
    print('The student\'s assignment list: ', phoebe.assignments)

    print('___________________________________________________________________________')
    print('Doing the assignment.')

    phoebe.do_assignment(writing_skills, essay)
    phoebe.hand_in_assignment(writing_skills, essay)
    print('The student\'s finished assignments: ', phoebe.finished)

    print('___________________________________________________________________________')
    print('Grading')

    monica.grade_assignment(phoebe, essay, 99)
    print(monica.graded)
    print('The student\'s grades: ', phoebe.grades)









