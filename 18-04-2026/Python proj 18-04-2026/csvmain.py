import csv
with open("data.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
#to read as dictionary
with open("data.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["name"],row["marks"])
#to write
data=[["name","marks"],["Priya",88],["Karan",75]]

with open("output.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(data)