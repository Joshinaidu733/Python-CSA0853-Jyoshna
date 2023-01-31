import math
a=int(input("enter A value"))
b=int(input("enter B value"))
c=int(input("enter C value"))
d=(b**2)-(4*a*c)
sol1=(-b+math.sqrt(d))/(2*a)
sol2=(-b-math.sqrt(d))/(2*a)
print(sol1)
print(sol2)

