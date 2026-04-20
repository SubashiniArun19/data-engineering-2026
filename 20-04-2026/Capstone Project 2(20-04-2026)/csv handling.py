import csv

file = open("attendance.csv", "r")
data = list(csv.reader(file))   # ✅ convert to list
data = data[1:]   # skip header
for row in data:
    print(row[0], row[1], row[2])
for row in data:
    name = row[0]
    present = int(row[1])
    total = int(row[2])
    percentage = (present / total) * 100
    print(name, ":", percentage)
for row in data:
    name = row[0]
    present = int(row[1])
    total = int(row[2])
    percentage = (present / total) * 100
    if percentage < 80:
        print(name)
best_name = ""
best_percentage = 0
for row in data:
    name = row[0]
    present = int(row[1])
    total = int(row[2])
    percentage = (present / total) * 100

    if percentage > best_percentage:
        best_percentage = percentage
        best_name = name
print("Best attendance:", best_name, best_percentage)
