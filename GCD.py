"""
Determine the greatest common divisor
of two numbers, e.g., GCD(8, 12) = 4
"""


import sys


def gcd(n1, n2, level=1):
    print(level, n1, n2)
    greatest_common_divisor = 0

    if n1 == n2:  # Base case: Numbers are equal
        greatest_common_divisor = n1
    else:  # Recursive case: Try again after subtracting
        # the smaller number from the larger number.
        if n1 > n2:  # n2 is smaller
            greatest_common_divisor = gcd(n1-n2, n2, level + 1)
        else:        # n1 is smaller
            greatest_common_divisor = gcd(n1, n2-n1, level + 1)
    return greatest_common_divisor


print(85, 98, 5, 85 * 98 * 5)

print('This program outputs the greatest '
      'common divisor of two numbers.\n')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if (num1 < 1) or (num2 < 1):
    print('Note: Neither value can be below 1.')
else:
    my_gcd = gcd(num1, num2)
    print('Greatest common divisor =', my_gcd)

print(sys.getrecursionlimit())
