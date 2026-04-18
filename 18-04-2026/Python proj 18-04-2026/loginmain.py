from collections import Counter
user=[]
with open("logins.txt","r") as file:
    for line in file:
        user.append(line.strip())
print(user)
#count of login records
print("total no of logins:",len(user))

user_counts=Counter(user)
for use,count in user_counts.items():
    print(use,":",count)
most_active_user=max(user_counts,key=user_counts.get)
print("most_active_user: ",most_active_user)
unique_users = set(user)
print("Unique users:")
for use in unique_users:
    print(use)