# Project Reflection

## 1. What was the hardest part of this project?

The hardest part of this project was implementing the registration logic while ensuring that duplicate registrations were prevented and course capacity limits were respected. Managing the relationships between students and courses required careful planning and testing.

## 2. Which classes did you create and why?

### Person

I created the Person class to store common information such as name, email, and phone number. This allowed me to demonstrate inheritance and reduce code duplication.

### Student

The Student class inherits from Person and adds a student ID. It represents individual students in the system.

### Course

The Course class stores course information including course ID, course name, trainer name, and capacity.

### SchoolSystem

The SchoolSystem class manages the application's main functionality. It handles adding students, adding courses, registrations, searching, viewing records, and file operations.

## 3. How does your registration logic prevent duplicate registrations?

Before registering a student, the system checks whether the student's ID already exists in the registration list for the selected course. If the student is already registered, the registration process stops and an appropriate message is displayed.

Example logic:

```python
if student_id in self.registrations[course_id]:
    print("Student is already registered for this course.")
```

## 4. How does your system check if a course is full?

The system compares the number of registered students with the course capacity. If the number of registered students is equal to or greater than the course capacity, the registration is rejected.

Example logic:

```python
if len(self.registrations[course_id]) >= course.capacity:
    print("Registration failed. This course is already full.")
```

## 5. What bugs did you face and how did you fix them?

### JSONDecodeError

Initially, the application crashed when loading empty JSON files. I fixed this by ensuring the JSON files contained valid default values such as:

```json
[]
```

for students and courses, and

```json
{}
```

for registrations.

### Duplicate Registration Bug

At first, students could register multiple times for the same course. I added a check to verify whether the student ID already existed in the course registration list.

### Input Validation Errors

The application initially accepted invalid data such as empty student IDs and invalid emails. I added validation checks before creating student and course records.

## 6. Which part of the code would you improve if you had more time?

If I had more time, I would:

* Add functionality to update and delete students and courses.
* Add an administrator login system.
* Record the date and time of each registration.
* Generate reports automatically.
* Improve the user interface and error messages.
* Store data in a database instead of JSON files for better scalability.

## What I Learned

This project helped me strengthen my understanding of:

* Classes and objects
* Inheritance
* File handling
* Dictionaries and lists
* Error handling
* Input validation
* Object-Oriented Programming design
* Building complete command-line applications