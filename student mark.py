M1=int(input("enter the mark"))
M2=int(input("enter the mark"))
M3=int(input("enter the mark"))
M4=int(input("enter the mark"))
avg=M1+M2+M3+M4/4
print("average ",avg)
if(avg>=91):
    print("grade : S")
elif(avg>=80 & avg <91):
    print("grade =A")
elif(avg>=70 & avg <80):
    print("grade =B")
elif(avg>=60 & avg <70 ):
    print("grade =B")
else:
    print("fail")
