list=[15,25,17,19,5,24,3]
mini=list[0]
for i in range(0,len(list)):
    if list[i]<mini:
        mini=list[i]
print(mini)
print(min(list))
