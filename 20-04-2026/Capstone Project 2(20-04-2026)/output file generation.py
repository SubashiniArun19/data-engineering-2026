import json
import csv
file = open("marks.json", "r")
marks_data = json.load(file)
file.close()
students = marks_data["students"]
file = open("attendance.csv", "r")
attendance_data = list(csv.reader(file))
file.close()
attendance_data = attendance_data[1:]
attendance_dict = {}
for row in attendance_data:
    name = row[0]
    present = int(row[1])
    total = int(row[2])
    percentage = (present / total) * 100
    attendance_dict[name] = percentage
combined = {}
for student in students:
    name = student["name"]

    combined[name] = {
        "marks": student["marks"],
        "attendance": attendance_dict[name],
        "course": student["course"]
    }
file = open("report.txt", "w")
file.write("Student Report\n\n")
for name in combined:
    marks = combined[name]["marks"]
    attendance = combined[name]["attendance"]
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    line = name + " - Marks: " + str(marks) + " - Attendance: " + str(attendance) + "% - Grade: " + grade + "\n"
    file.write(line)
file.close()
file = open("eligible_students.txt", "w")
for name in combined:
    marks = combined[name]["marks"]
    attendance = combined[name]["attendance"]
    if marks >= 75 and attendance >= 80:
        file.write(name + "\n")
file.close()