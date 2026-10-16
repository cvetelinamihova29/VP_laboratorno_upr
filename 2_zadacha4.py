n = int(input('Въведете число: '))
if n < 2: 
    print('Числото не е просто')
else: 
    prime = True

    for i in range(2, n): 
        if n % i == 0: 
            prime = False

if prime == True: 
    print('Числото е просто')
else: 
    print('Числото не е просто')