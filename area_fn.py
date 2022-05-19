n=0
l=0
b=0
h=0
r=0
def sqr(n):
	n=int(input("Enter the sides of square"))
	sq=n*n
	return(sq)
def rect(l,b):
	l=int(input("Enter the length of rectangle"))
	b=int(input("Enter the breadth of rectangle"))
	rect=l*b
	return(rect)
def tri(b,h):
	b=int(input("Enter the breadth of triangle"))
	h=int(input("Enter the height of triangle"))
	tri=(b*h)/2
	return(tri)
def cir(r):
	r=int(input("Enter the radius of circle"))
	cir=3.14*r*r
	return(cir)
print("Area of square=",sqr(n))
print("Area of rectangle=",rect(l,b))
print("Area of triangle=",tri(b,h))
print("Area of circle=",cir(r))
