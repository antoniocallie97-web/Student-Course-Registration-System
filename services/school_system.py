import json
from models.student import Student
from models.course import Course


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = {}

    # -----------------------------
    # STUDENT MANAGEMENT
    # -----------------------------

    def add_student(self):
        student_id = input("Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists.")
                return

        name = input("Name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone Number: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        if "@" not in email:
            print("Invalid email.")
            return

        if not phone:
            print("Phone number cannot be empty.")
            return

        student = Student(student_id, name, email, phone)
        self.students.append(student)

        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print("\n----------------")
            print(student)

    def search_student(self):
        keyword = input(
            "Enter Student ID or Name: "
        ).strip().lower()

        found = False

        for student in self.students:
            if (
                keyword == student.student_id.lower()
                or keyword in student.name.lower()
            ):
                print("\n----------------")
                print(student)
                found = True

        if not found:
            print("Student not found.")

    # -----------------------------
    # COURSE MANAGEMENT
    # -----------------------------

    def add_course(self):
        course_id = input("Course ID: ").strip()

        if not course_id:
            print("Course ID cannot be empty.")
            return

        for course in self.courses:
            if course.course_id == course_id:
                print("Course ID already exists.")
                return

        course_name = input("Course Name: ").strip()
        trainer = input("Trainer Name: ").strip()

        if not course_name:
            print("Course name cannot be empty.")
            return

        try:
            capacity = int(input("Capacity: "))

            if capacity <= 0:
                print("Capacity must be greater than 0.")
                return

        except ValueError:
            print("Capacity must be a number.")
            return

        course = Course(
            course_id,
            course_name,
            trainer,
            capacity
        )

        self.courses.append(course)

        print("Course added successfully.")

    def view_courses(self):
        if not self.courses:
            print("No courses found.")
            return

        for course in self.courses:
            print("\n----------------")
            print(course)

    # -----------------------------
    # REGISTRATION
    # -----------------------------

    def register_student(self):
        student_id = input("Student ID: ").strip()
        course_id = input("Course ID: ").strip()

        student = next(
            (
                s
                for s in self.students
                if s.student_id == student_id
            ),
            None,
        )

        course = next(
            (
                c
                for c in self.courses
                if c.course_id == course_id
            ),
            None,
        )

        if not student:
            print("Student not found.")
            return

        if not course:
            print("Course not found.")
            return

        if course_id not in self.registrations:
            self.registrations[course_id] = []

        if student_id in self.registrations[course_id]:
            print(
                f"{student.name} is already registered for this course."
            )
            return

        if len(self.registrations[course_id]) >= course.capacity:
            print(
                "Registration failed. This course is already full."
            )
            return

        self.registrations[course_id].append(student_id)

        print(
            f"{student.name} successfully registered for "
            f"{course.course_name}."
        )

    def view_students_in_course(self):
        course_id = input("Course ID: ").strip()

        if course_id not in self.registrations:
            print("No students registered.")
            return

        print("\nRegistered Students:")

        for student_id in self.registrations[course_id]:
            student = next(
                (
                    s
                    for s in self.students
                    if s.student_id == student_id
                ),
                None,
            )

            if student:
                print(
                    f"{student.student_id} - "
                    f"{student.name}"
                )

    def view_courses_for_student(self):
        student_id = input("Student ID: ").strip()

        print("\nRegistered Courses:")

        found = False

        for course_id, students in self.registrations.items():
            if student_id in students:

                course = next(
                    (
                        c
                        for c in self.courses
                        if c.course_id == course_id
                    ),
                    None,
                )

                if course:
                    print(
                        f"{course.course_id} - "
                        f"{course.course_name}"
                    )
                    found = True

        if not found:
            print("No registered courses.")

    # -----------------------------
    # FILE HANDLING
    # -----------------------------

    def save_data(self):
        with open(
            "data/students.json",
            "w"
        ) as file:
            json.dump(
                [s.to_dict() for s in self.students],
                file,
                indent=4,
            )

        with open(
            "data/courses.json",
            "w"
        ) as file:
            json.dump(
                [c.to_dict() for c in self.courses],
                file,
                indent=4,
            )

        with open(
            "data/registrations.json",
            "w"
        ) as file:
            json.dump(
                self.registrations,
                file,
                indent=4,
            )

        print("Data saved successfully.")

    def load_data(self):
        try:

            with open(
                "data/students.json",
                "r"
            ) as file:

                students_data = json.load(file)

                self.students = [
                    Student(
                        s["student_id"],
                        s["name"],
                        s["email"],
                        s["phone_number"]
                    )
                    for s in students_data
                ]

            with open(
                "data/courses.json",
                "r"
            ) as file:

                courses_data = json.load(file)

                self.courses = [
                    Course(
                        c["course_id"],
                        c["course_name"],
                        c["trainer_name"],
                        c["capacity"]
                    )
                    for c in courses_data
                ]

            with open(
                "data/registrations.json",
                "r"
            ) as file:

                self.registrations = json.load(file)

            print("Data loaded successfully.")

        except FileNotFoundError:
            print("No saved data found.")