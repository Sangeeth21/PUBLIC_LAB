n=input("Enter the string")

n =n.casefold()
r = reversed(n)
if list(n) == list(r):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
