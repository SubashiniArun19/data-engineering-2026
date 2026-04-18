num=[]
with open("numbers.txt","r") as file:
    for line in file:
        num.append(int(line))
print("Numbers")
print(num)
print("sum of numbers")
print(sum(num))
print("max of numbers")
print(max(num))
print("min of numbers")
print(min(num))
print("count of numbers which is greater than 5")
count=0
for n in num:
    if n>50:
        count+=1
print (count)