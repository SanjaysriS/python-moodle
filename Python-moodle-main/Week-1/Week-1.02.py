Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of his basic salary, and his house rent allowance is 20% of his basic salary. Write a program to calculate his gross salary.

Sample Input:

10000

Sample Output:

16000



For example:

Input	Result
10000
16000







def computesalary(basic):
    da=int(basic*0.4)
    ha=int(basic*0.2)
    gross=da+ha+basic
    return gross
basic=int(input())
print(computesalary(basic));
