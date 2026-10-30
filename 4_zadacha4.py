contacts = {}
for i in range(3): 
    name = input('Въведете име: ')
    phone = int(input('Въведете телефонен номер: '))
    contacts[name] = phone
search = input('Въведете име за търсене: ')
if search in contacts: 
    print('Телефон:', contacts[name])
else: 
    print('Невалидно име')