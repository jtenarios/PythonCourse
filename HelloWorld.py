# my_list=[1,3,4,5,2]
# another_list = ['hello', 'good bye']
# my_list.insert(-1,99)
# my_list.append(88)
#
# # salida = my_list.sort()
# # salida = my_list.reverse()
#
# print(my_list)

my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1, 2, 3, 4, 5]
my_list.sort()
my_list.reverse()

another_list.sort()
another_list.reverse()

print(my_list)
print(another_list)

final_list = my_list[-3:] + another_list[-3:]

print(final_list)

# ['d', 'b', 'a', 3, 2, 1]