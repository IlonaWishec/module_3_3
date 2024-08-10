def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # 1 строка True
print_params(2)  # 2 строка True
print_params(5, False)  # 5 False True
print_params(b=25)  # 1 25 True
print_params(c=[1, 2, 3])  # 1 строка [1, 2, 3]
values_list = [2, True, 'Dog']
values_dict = {'a': 2, 'b': 'cat', 'c': False}
print_params(*values_list)  # 2 True Dog
print_params(**values_dict)  # 2 cat False
values_list_2 = [4, 'rain']
print_params(*values_list_2, 42)  # 4 rain 42
