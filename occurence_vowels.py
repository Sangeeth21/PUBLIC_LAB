s=input("Enter the string:")
count1=0
count2=0
for i in s:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		count1=count1+1
	else:
		count2=count2+1
print("The number of occurence of vowels",count1,"The number of consonants",count2)
