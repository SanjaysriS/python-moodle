

mat=int(input())
phy=int(input())
che=int(input())
if (mat>=65 and phy>=55 and che>=50):
    print("The candidate is eligible")
elif (mat+phy+che>=180):
    print("The candidate is eligible")
else:
    print("The candidate is not eligible")
