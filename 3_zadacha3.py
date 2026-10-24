text = input('Въведете текст: ')
d1 = {}
for i in text: 
    if i in d1: 
        d1[i] +=1
    else: 
        d1[i] = 1

print('Речник:', d1)