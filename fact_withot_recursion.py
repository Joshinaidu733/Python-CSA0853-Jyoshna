n=int(input("enter a number to find factorial"))
fact=1
for i in range(2,n+1):
    fact=fact*i
print("the factorial of a number",fact)
