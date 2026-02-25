import json
import os

FILE_NAME= "students.json"

def load_students():
    #Reads students from the JSON file and returns a list
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r")as file:
            return json.load(file)
        
    except(json.JSONDecodeError, FileNotFoundError):
        return[]
    

def save_students(students_list):
    #Writes the student list into the JSON file
    try:
        if not isinstance(students_list, list):
             return False
        
        with open(FILE_NAME, "w")as file:
            json.dump(students_list, file, indent=4)
        return True

    except Exception:
        return False
    
    