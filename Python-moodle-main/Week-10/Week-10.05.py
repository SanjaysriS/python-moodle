def find_peak_elements(n, arr):
    peak_elements = []

    if n == 1:
        peak_elements.append(arr[0])
    elif arr[0] >= arr[1]:
        peak_elements.append(arr[0])

    for i in range(1, n - 1):
        if arr[i - 1] <= arr[i] >= arr[i + 1]:
            peak_elements.append(arr[i])

    if arr[n - 1] >= arr[n - 2]:
        peak_elements.append(arr[n - 1])

    return peak_elements

# Input handling
n = int(input())
arr = list(map(int, input().split()))

# Finding peak elements
peak_elements = find_peak_elements(n, arr)

# Output peak elements separated by space
print(" ".join(map(str, peak_elements)))
