# Creando un iterador

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# Iterando un iterador

# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#     except StopIteration:
#         break

for element in my_list:
    print(element)

# Cuando no quedan datos, la excepción StopIteration se lanza