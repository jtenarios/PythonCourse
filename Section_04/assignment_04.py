# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:
def grow_string(word):
    word_length = len(word)
    result = ''

    for i in range(word_length):
        result = result + word[0:i+1]

    print(result)
    return result

grow_string('Code') #→ 'CCoCodCode'
grow_string('abc') #→ 'aababc'
grow_string('ab') #→ 'aab'

































# Solution:

# def grow_string(str):
#   result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result

