# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:
def string_match(str_a, str_b):
    cont =0

    len_a = len(str_a)
    len_b = len(str_b)

    # Para repetir el bucle con el que tenga menos iteraciones, ya que el resto no importaria
    len_final = min(len_a, len_b)

    for i in range(len_final - 1):
        sub_str_a = str_a[i:i+2]
        sub_str_b = str_b[i:i+2]

        # print(str(i) + ' ' + sub_str_a)
        # print(str(i) + ' ' + sub_str_b)

        if sub_str_a == sub_str_b:
            cont += 1
    return cont

print(string_match('xxcaazz', 'xxbaaz')) #→ 3
print(string_match('abc', 'abc')) #→ 2
print(string_match('abc', 'axc')) #→ 0)






























# Solution
# def string_match(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0
#
#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter - 1):
#         a_sub = a[i:i + 2]
#         b_sub = b[i:i + 2]
#         if a_sub == b_sub:
#             count = count + 1
#
#     return count
