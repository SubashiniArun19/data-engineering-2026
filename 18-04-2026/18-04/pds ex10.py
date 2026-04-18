logins = [
("Rahul","10:00"),
("Sneha","10:10"),
("Rahul","11:00"),
("Arjun","11:15"),
("Sneha","11:30")
]
timesoflogincount={}
for login,times in logins:
    if login in timesoflogincount:
        timesoflogincount[login]+=1
    else:
        timesoflogincount[login]=1
print(timesoflogincount)
