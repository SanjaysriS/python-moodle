



num = int(input())
binary_str = bin(num)[2:]  # Convert to binary and remove '0b' prefix
count_ones = binary_str.count('1')
print(count_ones)
