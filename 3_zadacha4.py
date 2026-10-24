number = int(input('Въведете цяло число: '))
l1 = list(range(1, number+1))
print('Списък:', l1)
d1 = {}
for i in range(len(l1)): 
    key = l1[i]
    value = l1[-(i + 1)]
    d1[key] = value
print('Речник', d1)