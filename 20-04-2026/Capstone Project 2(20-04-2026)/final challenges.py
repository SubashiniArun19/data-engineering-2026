import json
import csv
def load_marks():
    file = open("marks.json", "r")
    data = json.load(file)
    file.close()
    return data["students"]
def load_attendance():
    file = open("attendance.csv", "r")
    data = list(csv.reader(file))
    file.close()
    return data[1:]
def get_topper(students):
    top = students[0]
    for s in students:
        if s["marks"] > top["marks"]:
            top = s
    return top["name"]
def get_best_attendance(attendance):
    best_name = ""
    best_percent = 0
    for row in attendance:
        name = row[0]
        percent = (int(row[1]) / int(row[2])) * 100
        if percent > best_percent:
            best_percent = percent
            best_name = name
    return best_name
def get_average_marks(students):
    total = 0
    for s in students:
        total += s["marks"]
    return round(total / len(students), 1)
def get_eligible_students(students, attendance):
    attendance_dict = {}
    for row in attendance:
        name = row[0]
        percent = (int(row[1]) / int(row[2])) * 100
        attendance_dict[name] = percent
    eligible = []
    for s in students:
        name = s["name"]
        if s["marks"] >= 75 and attendance_dict[name] >= 80:
            eligible.append(name)
    return eligible
def get_improvement_students(students, attendance):
    attendance_dict = {}
    for row in attendance:
        name = row[0]
        percent = (int(row[1]) / int(row[2])) * 100
        attendance_dict[name] = percent
    improve = []
    for s in students:
        name = s["name"]
        if s["marks"] < 75 or attendance_dict[name] < 80:
            improve.append(name)
    return improve
students = load_marks()
attendance = load_attendance()
topper = get_topper(students)
best_att = get_best_attendance(attendance)
avg = get_average_marks(students)
eligible = get_eligible_students(students, attendance)
improve = get_improvement_students(students, attendance)
print("Topper:", topper)
print("Best Attendance:", best_att)
print("Average Marks:", avg)
print("Eligible Students:", ", ".join(eligible))
print("Students Needing Improvement:", ", ".join(improve))