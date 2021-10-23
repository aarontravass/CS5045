L = [i for i in range(0, 40)]

even_dict = {'sum': 0}
odd_dict = {'sum': 0}
even_list = [even_dict.update({'sum': (i + even_dict['sum'])}) for i in L if i % 2]
odd_list = [odd_dict.update({'sum': (i + odd_dict['sum'])}) for i in L if not i % 2]
print("sum of even numbers is",even_dict['sum'])
print("sum of odd numbers is",odd_dict['sum'])