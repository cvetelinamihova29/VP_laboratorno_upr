def addition(a, b): 
    return a + b
def substraction(a, b): 
    return a - b
def multiplication(a, b): 
    return a * b
def division(a, b): 
    if b != 0: 
        return a / b
    else: 
        return 'Невалидно число'
opr = input('Въведете операция(+, -, *, /) ')
a = float(input('Въведете число: '))
b = float(input('Въведете второ число: '))
if opr == '+': 
    print(addition(a, b))
elif opr == '-': 
    print(substraction(a, b))
elif opr == '*': 
    print(multiplication(a, b))
elif opr == '/': 
    print(division(a, b))
else: 
    print('Невалидна операция')