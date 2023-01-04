# def reminder(arg1, arg2):
#     '''
#     :param arg1:
#     :param arg2:
#     :return: module arg1 and arg2
#     '''
#     return arg1%arg2
#
# my_reminder = reminder(10,3)
#
# print(my_reminder)


def test_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return 0

test_function(1, 2, 3, 'a', 'b', name='Jaime', age='37')