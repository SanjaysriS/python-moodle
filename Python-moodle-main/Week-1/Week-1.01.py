Write a program to convert strings to an integer and float and display its type.

Sample Input:

10

10.9

Sample Output:

10,<class 'int'>

10.9,<class 'float'>



For example:

Input	Result
10
10.9
10,<class 'int'>
10.9,<class 'float'>

a=input()
b=input()
a=int(a)
b=float(b)
b=round(b,1)
print(a,end=',')
print(type(a))
print(b,end=',')
print(type(b))


