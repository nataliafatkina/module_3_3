def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2,4)
print_params(65,'say',21.7)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_lis = [5, 'hello', True]
values_dict = {'a': 23, 'b': False, 'c': 'Types'}

print_params(*values_lis)
print_params(**values_dict)

values_list_2 = [11.234, True ]
print_params(*values_list_2, 42)