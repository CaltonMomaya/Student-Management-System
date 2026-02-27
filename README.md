# Student Management System (CLI - Python)

## Project Description
The Student Management System is a Command Line Interface (CLI) application developed using Python.  
The system allows users to manage student records by adding, updating, deleting, and viewing student information.
## Features
- Add a new student
- Update student information
- Delete a student
- View all students
- Save student data permanently using JSON file
- Load saved data when the program starts



## Project Structure


Project/
│
├── Crud/
│ └── student.py # Student CRUD operations
│
├── logic/
│ └── storage.py # File handling (JSON storage)
│
├── menu/
│ └── main.py # Program menu and flow control
│
└── students.json # Stored student data


---

## Team Responsibilities

### Member 1 – Student Logic
- Implemented student operations:
  - Add student
  - Update student
  - Delete student

### Member 2 – File Handling
- Managed data storage using JSON
- Implemented loading and saving student records
- Handled missing or empty files

### Member 3 – Menu & Program Flow
- Created CLI menu interface
- Handled user input
- Connected all modules together
- Controlled application execution flow

---

## Technologies Used
- Python 3
- JSON File Storage
- Command Line Interface (CLI)
- GitHub for collaboration

---

## How to Run the Project

1. Clone the repository:

git clone <repository-link>


2. Navigate to the project folder:

cd Project


3. Run the program:

python3 -m menu.main
---

## Example Student Format

```python
{
    "id": "101",
    "name": "John",
    "age": "20",
    "course": "CS"
}









