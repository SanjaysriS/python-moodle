n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
tot=sum(arr)
left=0
right=tot
for i in range(n):
    right-=arr[i]
    if left==right:
        print(i)
        break
    left+=arr[i]
