ALL_COURSES = [
    "Data Science",
    "Software Engineering",
    "DevOPS",
    "Cyber Security",
    "AI Engineering",
    "High School Bootcamp",
    "Product Design",
    "Data Analytics",
    "Data Analytics for HR Professionals",
]

ALLOWED_GENDERS = ["Male", "Female", "Other"]


class Student:
    student_count = 0
    all_students = []

    def __init__(
        self, first_name, last_name, age, gender, student_id, course, instructor
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.course = course
        self.instructor = instructor

        Student.student_count += 1
        Student.all_students.append(self)

    # -------------------------------
    # FIRST NAME getter/setter
    # -------------------------------
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("First name must be a non-empty string")
        self._first_name = value

    # -------------------------------
    # LAST NAME getter/setter
    # -------------------------------
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Last name must be a non-empty string")
        self._last_name = value

    # -------------------------------
    # AGE getter/setter
    # -------------------------------
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if int(value) < 18:
            raise ValueError("Age must be above 18 years")
        self._age = value

    # -------------------------------
    # GENDER getter/setter
    # -------------------------------
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in ALLOWED_GENDERS:
            raise ValueError("Gender must be Male, Female, or Other")
        self._gender = value

    # -------------------------------
    # COURSE getter/setter
    # -------------------------------
    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if value in ALL_COURSES:
            self._course = value
        else:
            raise ValueError("The course listed is not offered yet")

    # -------------------------------
    # Other properties/methods
    # -------------------------------
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    @classmethod
    def total_students(cls):
        return f"The total number of students is: {cls.student_count}"

    @classmethod
    def student_list(cls):
        return [f"{student.first_name} {student.last_name}" for student in cls.all_students]

    @staticmethod
    def reverse_name(first_name, last_name):
        return f"{last_name} {first_name}"


# -------------------------------
# Student Objects
# -------------------------------
student1 = Student("Bradley", "Murimi", 40, "Male", "MSS-1234", "Software Engineering", "Fainus Mudahe")
student2 = Student("Mariam", "Rashid", 20, "Female", "MSS-1428", "Software Engineering", "Julius Mutindwa")
student3 = Student("Fredrick", "Rangara", 50, "Male", "MSS-1480", "Software Engineering", "Julius Mutindwa")

# THIS WILL THROW AN ERROR (course not offered)
student4 = Student("Adonis", "Pierre", 30, "Male", "MSS-3445", "Bio Tech", "Julius Mutindwa")

print(student2.course)
