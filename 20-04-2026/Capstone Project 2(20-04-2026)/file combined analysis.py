import json
import csv
file = open("marks.json", "r")
marks_data = json.load(file)
file.close()
students = marks_data["students"]
file = open("attendance.csv", "r")
attendance_data = list(csv.reader(file))
file.close()
attendance_data = attendance_data[1:]  # skip header
attendance_dict = {}
for row in attendance_data:
    name = row[0]
    present = int(row[1])
    total = int(row[2])
    percentage = (present / total) * 100
    attendance_dict[name] = percentage
combined = []
combin = {}
print("Full Student Report:\n")
for student in students:
    name = student["name"]

    combin[name] = {
        "marks": student["marks"],
        "attendance": attendance_dict[name],
        "course": student["course"]
    }

print("Combined Data:")
print(combin)
for student in students:
    name = student["name"]

    record = {
        "name": name,
        "marks": student["marks"],
        "course": student["course"],
        "attendance": attendance_dict[name]
    }

    combined.append(record)

for s in combined:
    marks = s["marks"]

    # grade logic
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(
        s["name"],
        "| Marks:", s["marks"],
        "| Attendance:", s["attendance"],
        "| Course:", s["course"],
        "| Grade:", grade
    )
print("\nEligible for Certification:")
for s in combined:
    if s["marks"] >= 75 and s["attendance"] >= 80:
        print(s["name"])
print("\nNeeds Improvement:")

for s in combined:
    if s["marks"] < 75 or s["attendance"] < 80:
        print(s["name"])