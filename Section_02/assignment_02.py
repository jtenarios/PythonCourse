# Assignment 2:
"""
Using some of the collection data types we learned about
in the course so such as a list and dictionary, create a
data structure that best represents the following scenario:

Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""

# your code below:
tom_objects = ['jacket', 'car', 'TV']
mike_objects = ['bike', 'laptop', 'boat']
my_list = [ {'Tom' : {'age': 22, 'salary': 20000, 'objects': tom_objects }},
            {'Mike' : {'age': 27, 'salary': 24000, 'objects': mike_objects }} ]

my_list3 = {
            'Tom' : {'age': 22, 'salary': 20000, 'objects': tom_objects },
            'Mike' : {'age': 27, 'salary': 24000, 'objects': mike_objects }
           }

print(my_list[0])
print(my_list3.get('Tom'))





















































# Solution

# my_list = [{'Tom': {'salary': 20000, 'age': 22, 'owns': ['jacket', 'car', 'TV']}},
#            {'Mike': {'salary': 24000, 'age': 27, 'owns': ['bike', 'laptop', 'boat']}}]
