

def merge_arrays(arr1, arr2):
    
    merged_array = arr1 + arr2
    
    merged_array = list(set(merged_array))
    return merged_array


n1 = int(input())
array1 = []
for _ in range(n1):
    array1.append(int(input()))


n2 = int(input())
array2 = []
for _ in range(n2):
    array2.append(int(input()))


merged = merge_arrays(array1, array2)
merged.sort()  
for i in merged:
    print(i, end=" ")
