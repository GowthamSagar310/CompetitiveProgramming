def function(n):
    num = 0
    for i in range(31, -1, -1):
        num += (n & 1) * (2 ** i)
        n = n >> 1
        if n == 0: break
    return num

# neetcode solution
def another_approach(n):
    res = 0 # every bit is 0     
    # 5           000...101 
    # reversed 5  101...000
    # get each set_bit in n and place it in exactly opposite position in res 
    for i in range(32):
        # 0th bit of n should 31st bit of res 
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    return res 
    


n = int(input())
print(another_approach(n))