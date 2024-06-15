s1 = input()
s2 = input()
r = ''
for c in s1:
    if c not in s2:
        r += c
print(r)  

