




a=int(input())
b=int(input())
x=float(a*0.100)
y=float(b*0.250)
refund=float(round((x+y),2))
print("Your total refund will be $",end="")
print("{:.2f}".format(refund),end='.')
