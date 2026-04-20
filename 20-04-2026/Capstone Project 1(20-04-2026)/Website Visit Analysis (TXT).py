with open("website_visits.txt","r") as file:
    data=file.read().splitlines()
print("All Visitors")
for d in data:
    print(d)
print("Total Visits")
print(len(data))
uniq=set(data)
print("Unique Visits")
print(uniq)
print("Visits per Customer")
visits={}
for d in data:
    if d in visits:
        visits[d]+=1
    else:
        visits[d]=1
print(visits)
maxvisitor=max(visits,key=visits.get)
print("Most frequenyt visitor:",maxvisitor,"")