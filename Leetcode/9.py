def palindrome(x):
    temp = x
    rev = 0
    while x > 0:
        digit = x % 10
        rev = rev * 10 + digit        
        x = x // 10 
    return temp == rev 

x = int(input())
print(palindrome(x))