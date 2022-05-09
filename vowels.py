def replaceVowelsWithX(n, X):
    vowels = 'AEIOUaeiou'
    for ele in vowels:
        n = n.replace(ele, X)
    return n
a=input("Enter the string")
X = "X"
print("Given String:", a)
print("Given Specified Character:", X)
print("After replacing vowels with the specified character:",replaceVowelsWithX(a, X))
