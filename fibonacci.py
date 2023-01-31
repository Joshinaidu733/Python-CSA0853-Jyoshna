n=int(input("enter the range of number"))
a=0
b=1
for i in range(n):
        c=a+b
        if(c<=n):
            print(c)
            a=b
            b=c

