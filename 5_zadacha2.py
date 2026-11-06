def reverse(a): 
    if a < 0: 
        text = str(abs(a))
        return -int(text[::-1])
    else: 
        text = str(a)
        return int(text[::-1])
def palindrome(a): 
    if a == reverse(a): 
        return 1
    else: 
        return 0
a = int(input('Въведете число: '))
print(palindrome(a))