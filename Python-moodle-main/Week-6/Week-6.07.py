a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
c={x:b.count(x) for x in b} 
for i in c:
    print(i,"occurs",c[i],"times")
