mark=int(input("Enter mark: "))
if mark>=90:
    print(" A Grade")
elif mark<=89 and mark>=70:
    print(" B Grade")
elif mark<=69 and mark>=50:
    print("C Grade")
else:
    print("Fail")