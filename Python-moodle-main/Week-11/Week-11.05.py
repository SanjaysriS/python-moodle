def age(n):
    l=[str(i) for i in range(10)]
    flag=0
    for i in n:
        if i not in l:
            flag=1
            break
    if flag:
         return "Error: Please enter a valid age."
    else:
        return f"You are {n} years old."
while True :
    try :
        n=input()
        print(age(n))
        break
    except EOFError:
        print("Error: Please enter a valid age.")
        break
