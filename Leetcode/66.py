digits = [9,9,9]
carry = 1
for i in range(len(digits)-1,-1,-1):
    digits[i] += carry
    if digits[i] > 9:
        digits[i] %= 10
        carry = 1
    else:
        carry = 0
if carry: digits = [1] + digits
print(digits)