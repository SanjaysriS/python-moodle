def count_frequency(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

def display_sorted_frequency(frequency):
    sorted_frequency = sorted(frequency.items())
    for num, freq in sorted_frequency:
        print(num, freq)

# Accept input from the user
numbers = list(map(int, input().split()))

# Count frequency of numbers
frequency = count_frequency(numbers)

# Display sorted frequency
display_sorted_frequency(frequency)
