def calculate_lcm(n, m):
    if n > m:  
        greater = n 
    else:
        greater = m
    while(True): 
        if((greater % n == 0) and (greater % m == 0)):  
            lcm = greater
            break
        greater += 1
    return lcm
n = int(input("Enter first number: "))  
m = int(input("Enter second number: "))
print("The L.C.M. of", n,"and", m,"is", calculate_lcm(n, m))  
