def sort_dict_by_value_sum():
    # Read number of entries
    n = int(input())
   
    # Initialize the dictionary
    test_dict = {}
   
    # Read each entry
    for _ in range(n):
        entry = input().split()
        key = entry[0]
        values = list(map(int, entry[1:]))
        test_dict[key] = values
   
    # Calculate sum of values for each key
    sum_dict = {key: sum(values) for key, values in test_dict.items()}
   
    # Sort dictionary by the sum of values
    sorted_sum_dict = dict(sorted(sum_dict.items(), key=lambda item: item[1]))
   
    # Print the sorted dictionary with sums
    for key, value_sum in sorted_sum_dict.items():
        print(f"{key} {value_sum}")

if __name__ == "__main__":
    sort_dict_by_value_sum()
