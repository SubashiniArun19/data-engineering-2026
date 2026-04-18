numbers = [10,20,10,30,20,10,40]
count={}
for i in numbers:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

from collections import Counter
freq1=dict(Counter(numbers))
print(freq1)