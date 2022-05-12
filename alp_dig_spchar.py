s = input("Enter the String : ")
alphabets=0
digits=0
special=0
for i in range(len(s)):
    if(s[i].isalpha()):
        alphabets = alphabets + 1
    elif(s[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)
