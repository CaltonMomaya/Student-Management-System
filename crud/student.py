# student.py

def add_student(students, new_student):
    students.append(new_student)
    return students


def update_student(students, student_id, updated_data):
    for student in students:
        if student["id"] == student_id:
            student.update(updated_data)
            return True
    return False


def delete_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return True
    return False