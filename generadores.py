def my_gen():
    """Un ejemplo de generadores"""

    print('Hello World!')
    n = 0
    yield n

    print('Hello heaven!')
    n = 1
    yield n

    print('Hello hell!')
    n = 2
    yield n

a = my_gen()
print(next(a)) # Hello World!
print(next(a)) # Hello heaven!
print(next(a)) # Hello hell!
print(next(a)) # StopIteration