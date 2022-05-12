str=input("Enter the string:")
b=""
for i in str:
    if (i not in b):
        b=b+i
print(b)

