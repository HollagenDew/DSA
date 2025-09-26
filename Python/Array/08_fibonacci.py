# Author: Prateek Waghmare
# Description: Generates a Fibonacci series of given length.
# Time Complexity: O(n) | Space Complexity: O(1)

num1, num2 = 0, 1
n = int(input("Enter the length of Fibonacci series: "))

print(num1)
print(num2)

for _ in range(n - 2):
    fib = num1 + num2
    print(fib)
    num1, num2 = num2, fib