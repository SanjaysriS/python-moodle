def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Accept input from the user
n = int(input())
arr = list(map(int, input().split()))

# Perform bubble sort
bubble_sort(arr)

# Print the sorted list
print(*arr)
