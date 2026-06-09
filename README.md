# Student Course Registration System

## Project Description

The Student Course Registration System is a command-line Python application designed to help a training school manage students, courses, and course registrations. The system allows an administrator to add students, create courses, register students to courses, and store information using JSON files.

## Features Implemented

* Add new students
* View all students
* Search students by ID or name
* Add new courses
* View all courses
* Register students to courses
* Prevent duplicate student IDs
* Prevent duplicate course IDs
* Prevent duplicate course registrations
* Prevent registration when a course is full
* View students registered in a course
* View courses registered by a student
* Save data to JSON files
* Load data from JSON files
* Error handling and input validation

## Classes Used

### Person

Base class containing common attributes:

* Name
* Email
* Phone Number

### Student

Inherits from Person and adds:

* Student ID

### Course

Stores:

* Course ID
* Course Name
* Trainer Name
* Capacity

### SchoolSystem

Handles:

* Student management
* Course management
* Registration management
* File handling

## How to Run the Project

1. Open a terminal.
2. Navigate to the project folder.

```bash
python main.py
```

or

```bash
python3 main.py
```

3. Follow the menu prompts.

## File Structure

student-course-registration/

* main.py
* models/

  * person.py
  * student.py
  * course.py
* services/

  * school_system.py
* data/

  * students.json
  * courses.json
  * registrations.json

## Technologies Used

* Python 3
* JSON File Storage
* Object-Oriented Programming

## Author

Student Course Registration System Project
