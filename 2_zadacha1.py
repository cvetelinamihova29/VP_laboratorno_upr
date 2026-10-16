n = int(input('Въведете брой цели числа '))
max_num = int(input('Въведете число '))

for i in range(n-1): 
    num = int(input('Въведете число: '))
    if num > max_num: 
        max_num = num

print('Най-голямото число е', max_num)