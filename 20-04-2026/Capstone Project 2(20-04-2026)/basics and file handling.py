file = open("students.txt", "r")
names = file.readlines()
for name in names:
    print(name.strip())
print("Total entries:", len(names))
unique_names = set()
for name in names:
    unique_names.add(name.strip())
print("Unique students:", unique_names)
count_dict = {}
for name in names:
    name = name.strip()
    if name in count_dict:
        count_dict[name] += 1
    else:
        count_dict[name] = 1
print(count_dict)
new_file = open("unique_students.txt", "w")
for name in unique_names:
    new_file.write(name + "\n")
file.close()
new_file.close()