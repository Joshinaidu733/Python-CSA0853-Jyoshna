n=int(input("enter a number to find factorial"))
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
result=fact(n)
print("the factorial of number",result)
