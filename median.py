a=[]
b=int(input("Enter Number of Elements:"))
for i in range(1,b+1):
    c=int(input("enter the num "))
    print(a.append(c))
    a.sort()
print("Median Element is:",a[int((b-1)/2)])
