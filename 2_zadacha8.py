min = int(input('Въведете долна граница: '))
max = int(input('Въведете горна граница: '))
num = 0
for i in range(10): 
    numm = int(input('Въведете число: '))
    if numm >= min and numm <= max: 
        num +=1 
print('Броят на числата в интервала е', num)