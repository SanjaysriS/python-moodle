
S1 = input()
S2 = input()
N = int(input())
common_chars = ""
for char in S1:
    if char in S2 and char not in common_chars:
        common_chars += char
        if len(common_chars) == N:
            break
print(common_chars)
