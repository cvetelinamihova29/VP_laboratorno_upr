text = input('Въведете текст: ').lower()
count = {}
for char in text: 
    if char != ' ': 
        if char in count: 
            count[char] += 1
        else: 
            count[char] = 1

max_count = 0
most_common = []

for char in count: 
    if count[char] > max_count: 
        max_count = count[char]
        most_common.append(char)
    elif count[char] == max_count: 
        most_common.append(char)

print('Най-често срещаният символ е', most_common)
print('Среща се', max_count, 'пъти')