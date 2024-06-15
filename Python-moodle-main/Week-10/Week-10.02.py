def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return swaps

# Accept input from the user
n = int(input())
arr = list(map(int, input().split()))

# Perform bubble sort and count swaps
num_swaps = bubble_sort(arr)

# Print the required output
print(f"List is sorted in {num_swaps} swaps.")
print(f"First Element: {arr[0]}")
print(f"Last Element: {arr[-1]}")

print("Last Element:", arr[-1])



