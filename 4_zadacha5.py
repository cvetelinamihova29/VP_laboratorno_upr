numbers = input('Въведете списък от числа: ').split()
new_list = []
for x in numbers: 
    if int(x) not in new_list: 
        new_list.append(int(x))

print(new_list)