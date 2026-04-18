with open("data.txt", "r") as file:

    for line in file:
        print(line.strip())

    students=file.readlines()
print("Total students:", len(students))
with open("data.txt", "w") as file:
    file.write("Total students\n")
    file.write("Student List\n")
#this"w"  write mode will overwrite
with open("data.txt", "a") as file:
    file.write("Arjun\n")
    file.write("Priya\n")
    file.write("Rahul\n")
    #this"a" append mode write will add the data in the existing file in the last4
languages=["Python\n","Java\n","C++\n","C#\n"]
with open("data.txt", "w") as file:
    file.writelines(languages)
#this writeline helps to write multiple lines


