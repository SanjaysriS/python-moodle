

number = int(input())
if abs(number) < 10:
    print(-1)
else:
    second_last = abs(number) // 10 % 10
    print(second_last)
