n = int(input())
nums = list(map(int, input().split()))
k = int(input())
freq = {}
count = 0
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for num in freq:
    if k == 0:
        count += freq[num] * (freq[num] - 1) // 2  # Corrected division to integer division
    else:
        if num + k in freq:
            count += freq[num] * freq[num + k]
print(count)
