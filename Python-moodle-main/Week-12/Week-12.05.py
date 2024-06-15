def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Input
n = int(input())

# Check if n is a power of two
result = is_power_of_two(n)

# Output
print(result)
