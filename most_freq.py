str=input("Enter the string:")
print(str)

char_freq={}

for i in str:
    if i in char_freq:
        char_freq[i]=char_freq[i]+1
    else:
        char_freq[i]= 1
result= max(char_freq, key = char_freq.get)

print("Most frequent character: ",result)