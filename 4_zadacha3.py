number = int(input('Въведете цяло число: '))
words = input('Въведете списък от думи: ').split()
result = []
for word in words: 
    if len(word) >= number: 
        result.append(word)

result_tuple = tuple(result)
print('Думи с дължина, >=', number, result_tuple)