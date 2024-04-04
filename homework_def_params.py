def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(a=2, b=7, c='wow')
print_params(a=2, b=7)
#print_params(a=2, b=7, c='wow', v=34)  - выдает ошибку "print_params() got an unexpected keyword argument 'v'"

values_list = ['первый тип', False, 67]
values_dict = {'a': 1, 'b': 'пельмень', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["helicopter", True]
print_params(*values_list_2, 42)

