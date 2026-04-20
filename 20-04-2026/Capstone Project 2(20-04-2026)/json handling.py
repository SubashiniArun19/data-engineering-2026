import json
file = open("marks.json", "r")
data = json.load(file)
for student in data["students"]:
    print(student["name"], student["marks"])
top_student = data["students"][0]
for student in data["students"]:
    if student["marks"] > top_student["marks"]:
        top_student = student
print("Highest:", top_student["name"], top_student["marks"])
low_student = data["students"][0]
for student in data["students"]:
    if student["marks"] < low_student["marks"]:
        low_student = student
print("Lowest:", low_student["name"], low_student["marks"])
total = 0
for student in data["students"]:
    total += student["marks"]
avg = total / len(data["students"])
print("Average marks:", avg)
for student in data["students"]:
    if student["course"] == "Python":
        print(student["name"])
course_count = {}
for student in data["students"]:
    course = student["course"]
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1
print(course_count)