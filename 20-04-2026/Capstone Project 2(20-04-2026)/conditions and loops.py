import json
import csv
file = open("marks.json", "r")
data = json.load(file)
file.close()
file = open("attendance.csv", "r")
data_csv = list(csv.reader(file))
data_csv = data_csv[1:]
attendance_dict = {}
for row in data_csv:
    name = row[0]
    present = int(row[1])
    total = int(row[2])
    percentage = (present / total) * 100
    attendance_dict[name] = percentage
print("Pass/Fail:")
for student in data["students"]:
    name = student["name"]
    marks = student["marks"]

    if marks >= 50:
        print(name, "Pass")
    else:
        print(name, "Fail")
print("\nGrades:")
for student in data["students"]:
    name = student["name"]
    marks = student["marks"]
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    print(name, ":", grade)
print("\nHigh performers (marks > 80 AND attendance > 85%):")
for student in data["students"]:
    name = student["name"]
    marks = student["marks"]
    attendance = attendance_dict[name]
    if marks > 80 and attendance > 85:
        print(name)