Write a python program that takes a integer between 0 and 15 as input and displays the number of '1' s in its binary form.(Hint:use python bitwise operator.

Sample Input

3

Sample Output:

2

Explanation:

The binary representation of 3 is 011, hence there are 2 ones in it. so the output is 2.


For example:

Input	Result
3
2





num = int(input())
binary_str = bin(num)[2:]  # Convert to binary and remove '0b' prefix
count_ones = binary_str.count('1')
print(count_ones)
