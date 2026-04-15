n=int(input("Enter a number"))
if n>0:
 f = 1
 for i in range(1, n + 1):
     f *= i
 print(f)
else:
    print("Invalid Number")