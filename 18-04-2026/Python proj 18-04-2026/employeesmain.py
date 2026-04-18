import csv
employees=[]
with open("employees.csv",'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row["name"])
        row["salary"]=int(row["salary"])
        employees.append(row)
print("employees in IT department")
for row in employees:
    if row["department"]=="IT":
        print(row["name"])
total=sum(employee["salary"] for employee in employees)
print("Avg salary")
print(total/len(employees))
maxsalary=max(employees ,key=lambda x:x["salary"])
print("Max salary",maxsalary)
empofdept={}
for row in employees:
    dept=row["department"]
    if dept in empofdept:
        empofdept[dept]+=1
    else:
        empofdept[dept]=1
print(empofdept)