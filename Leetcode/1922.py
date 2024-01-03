# https://leetcode.com/problems/count-good-numbers/description/


def count_good_numbers(n):
    MOD = 1_000_000_007
    num_even = (n+1)//2
    num_odd = n - num_even

    def bin_expo(number, power):
        if power == 0:
            return 1
        if power % 2 == 0: return (bin_expo(number, power // 2) ** 2) % MOD
        if power % 2 == 1: return (bin_expo(number, power-1) * number)  % MOD
        
    # ans = (5^num_even + 4^num_odd)
    ans = (bin_expo(5, num_even) * bin_expo(4, num_odd)) % MOD
    return ans 

n = int(input())
print(count_good_numbers(n))



