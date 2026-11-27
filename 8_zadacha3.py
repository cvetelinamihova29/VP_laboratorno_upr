try: 
    x = int(input('Въведете цяло число: '))
    if x < 0: 
        raise ValueError()
    print(x ** (1/2))
except ValueError: 
    print('Невалидно число')
finally: 
    print('Good Bye')