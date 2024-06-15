s=str(input())
n=int(input())
a=s.split()
l=len(a)
count=0
for i in a:
    p=len(i)
    if(p>=n):
        count+=1
print(count)
