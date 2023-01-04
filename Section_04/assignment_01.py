# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""

# Your Code Below:
def twelver (first_number, second_number):
    return (first_number == 12 or second_number == 12 or first_number + second_number ==12)

result = twelver(3, 12)
print(result)

result = twelver(3, 12)
print(result)

result = twelver(9, 3)
print(result)

result = twelver(4, 9)
print(result)









































# Solution:
# def twelver(a, b):
#   return (a == 12 or b == 12 or a+b == 12)