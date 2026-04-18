students = {
"Rahul":85,
"Sneha":92,
"Arjun":78,
"Priya":88
}
topper=max(students,key=students.get)
print(topper)
avg=sum(students.values())/len(students)
print(avg)
for name,mark in students.items():
    if mark>85:
        print(name)
    