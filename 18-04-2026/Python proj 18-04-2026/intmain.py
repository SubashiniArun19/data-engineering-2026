total=0
with open("data1.txt","r") as file:
    for line in file:
        total+=int(line.strip())
print("Total:",total)
