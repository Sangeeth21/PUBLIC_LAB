
def calculate_hcf(n, m):
	if n > m:  
		smaller = m  
	else:  
        	smaller = n  
	for i in range(1,smaller + 1):  
		if((n % i == 0) and (m % i == 0)):  
           	 hcf = i
	return hcf
n=input("Enter first number: ")
n=int(n)
m=input("Enter second number: ")
m=int(m)
print("The H.C.F. of", n,"and", m,"is", calculate_hcf(n, m))  
