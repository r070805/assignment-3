# task 1
import math

a=int(input("enter a number"))
def factorial(n):
    if n <2:
        return 1
    else:
        return n * (factorial(n-1))
result=factorial(a)
print("factorial of",a,"is:",result)
#task 2
b=int(input("enter a number :"))
s=math.sqrt(b)
l=math.log(b)
m=math.sin(b)
print("square root :",s)
print("logarithm :",l)
print("sine :",m)

