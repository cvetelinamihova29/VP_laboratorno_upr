def change(number, list): 
    for i in range(len(list)): 
        if list[i] > number: 
            list[i] = 0
    return list

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = 3
print(change(number, list_1))