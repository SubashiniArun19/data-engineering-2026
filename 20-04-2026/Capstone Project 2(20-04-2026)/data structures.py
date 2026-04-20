import json
import csv
file = open("marks.json", "r")
data = json.load(file)
file.close()
marks_list = []
for student in data["students"]:
    marks_list.append(student["marks"])
print("Marks list:", marks_list)
print("Highest:", max(marks_list))
print("Lowest:", min(marks_list))
print("Sum:", sum(marks_list))
courses = []
for student in data["students"]:
    courses.append(student["course"])
courses_tuple = tuple(courses)
print("Courses tuple:", courses_tuple)
courses_set = set(courses)
print("Unique courses:", courses_set)
marks_dict = {}
for student in data["students"]:
    marks_dict[student["name"]] = student["marks"]
print("Marks dict:", marks_dict)
file = open("attendance.csv", "r")
data_csv = list(csv.reader(file))
file.close()
data_csv = data_csv[1:]  # skip header
attendance_dict = {}
for row in data_csv:
    name = row[0]
    present = int(row[1])
    total = int(row[2])
    percentage = (present / total) * 100
    attendance_dict[name] = percentage
print("Attendance dict:", attendance_dict)