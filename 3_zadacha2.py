import random 
n = 6 
l1 = [random.randint(1, 10) for i in range(n)]
print('Оригинален списък:', l1)
l2 = []
for i in range(len(l1) - 1): 
    l2.append(l1[i])
    l2.append(l1[i] + l1[i+1])

l2.append(l1[:-1])
print('Нов списък:', l2)