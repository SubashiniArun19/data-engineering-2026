import json
import csv
def read_students():
    file = open("students.txt", "r")
    names = file.readlines()
    file.close()
    return [name.strip() for name in names]
def load_marks():
    file = open("marks.json", "r")
    data = json.load(file)
    file.close()
    return data["students"]
def load_attendance():
    file = open("attendance.csv", "r")
    data = list(csv.reader(file))
    file.close()
    return data[1:]   # skip header
def average_marks(students):
    total = 0
    for student in students:
        total += student["marks"]
    return total / len(students)
def attendance_percentage(present, total):
    return (present / total) * 100
def get_topper(students):
    top = students[0]
    for student in students:
        if student["marks"] > top["marks"]:
            top = student
    return top
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
