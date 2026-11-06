def square(a): 
    return a ** 2
def rectangle(a, b): 
    return a * b
def triangle(a, h): 
    return (a * h) / 2
print('Квадрат: 1, Правоъгълник: 2, Триъгълник: 3')
type = int(input('Въведете номер на фигура: '))
if type == 1: 
    a = float(input('Въведете страна: '))
    print('Лицето е', square(a))
elif type == 2: 
    a = float(input('Въведете първата страна: '))
    b = float(input('Въведете втората страна: '))
    print('Лицето е', rectangle(a, b))
elif type == 3: 
    a = float(input('Въведете страна: '))
    h = float(input('Въведете височина: '))
    print('Лицето е', triangle(a, h))