s= input()
w= s.split()
l = ""
m = 0
for w in w:
    if len(w) > m:
        l = w
        m = len(w)
print(l)
print(m)


