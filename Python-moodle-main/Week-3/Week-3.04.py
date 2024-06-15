



num1=int(input())
num2=int(input())
num3=int(input())
n1=num1*num1
n2=num2*num2
n3=num3*num3
if(n1+n2==n3):
    print("yes")
elif(n1+n3==n2):
    print("yes")
elif(n2+n3==n1):
    print("yes")
else:
    print("no")
