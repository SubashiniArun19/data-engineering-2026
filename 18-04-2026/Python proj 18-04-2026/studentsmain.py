import json
with open("students.json","r")as file:
    data = json.load(file)
for stud in data["students"]:
    print(stud["name"])
for stud in data["students"]:
    if stud["course"]=="Python":
        print(stud)
print("highest marks got by this student\n")
highmarkstud=max(data["students"],key=lambda x: x["marks"])
print(highmarkstud)
student=data["students"]
total=sum(stud["marks"] for stud in student)
avg=total/len(student)
print(avg)
count={}
for stud in student:
    course=stud["course"]
    if course in count:
        count[course]+=1
    else:
        count[course]=1
print(count)