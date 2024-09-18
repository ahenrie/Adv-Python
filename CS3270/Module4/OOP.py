# Object Oriented Python

a = 1
b = "What is up"
c = [3, 4, 5]

#print(type(a))
#print(type(b))
#print(type(c))

# Classes
# Before created class
school = {
    "name":"hogwarts",
    "student": ["harry", "ron", "Draco Malfoy"],
    "classes": ["history", "Potions"],
    "country": "United Kingdom"
}

class School:
    name = "Hogwarts"
    students = ["harry", "ron", "Draco Malfoy"]
    classes = ["history", "Potions"]
    country = "United Kingdom"

hogwarts = School()

#print(hogwarts.classes)


class OtherSchool:

    def __init__(self, name, country):
        self._name = name
        self._country = country
        self.students = []
        self.classes = []

    def add_class(self, class_name):
        self.classes.append(class_name)

    def add_multiple_class(self, class_list):
        for course in class_list:
            self.classes.append(course)

    def add_student(self, student):
        self.students.append(student)

    def add_multiple_students(self, student_list):
        for student in student_list:
            self.students.append(student)

    def pretty_print(self):
        # Print name and location
        print(f"School Name: {self._name}")
        print(f"Country: {self._country}")

        # Print students one by one
        print("Students: ", end="")
        (lambda students: print(*students))(self.students)

        # Print classes one by one
        print("Classes: ", end="")
        (lambda classes: print(*classes))(self.classes)

hogwarts_other = OtherSchool("Hog My Warts", "America")

students_to_add = ["a", "b", "c", "d"]
classes_to_add = ["classA", "classB", "classC"]

hogwarts_other.add_multiple_class(classes_to_add)
hogwarts_other.add_multiple_students(students_to_add)

hogwarts_other.pretty_print()
