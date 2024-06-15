# Accept input from the user
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Create sets from the arrays to find unique elements
set1 = set(arr1)
set2 = set(arr2)

# Find non-repeating elements
non_repeating = (set1.symmetric_difference(set2))

# Print the non-repeating elements and their count
if non_repeating:
    print(*non_repeating)
    print(len(non_repeating))
else:
    print("NO SUCH ELEMENTS")

