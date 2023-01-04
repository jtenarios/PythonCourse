# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

#Your Code Below:
def sum78(my_list):
    result = 0
    found_7 = False
    found_8 = False

    for i in list(my_list):
        if i == 7:
            found_7 = True
            found_8 = False
        elif i == 8 and found_7:
            found_7 = True
            found_8 = True

        if not found_7:
            result += i
        # elif found_7 and not found_8:
        #     pass
        elif found_8:
            found_7 = False
            found_8 = False

    return result

print(sum78([1, 2, 2])) #→ 5
print(sum78([1, 2, 2, 7, 99, 99, 8])) #→ 5
print(sum78([1, 1, 7, 8, 2])) #→ 4
print(sum78([1, 8, 1, 7, 1, 8, 2])) #→ 13



























# Solution:

# def sum78(nums):
#     sum = 0
#     inRange = False
#
#     for i in range(len(nums)):
#         if nums[i] == 7:
#             inRange = True
#
#         if not inRange:
#             sum += nums[i]
#
#         if inRange and nums[i] == 8:
#             inRange = False
#
#     return sum