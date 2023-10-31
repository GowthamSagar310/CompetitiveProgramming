# from math import floor
# n = int(input())
# s = (n * (n + 1)) // 2
# if s % 2 == 0 :
#     print("YES")
#     even = [i for i in range(1,n+1) if i % 2 == 0]
#     odd =  [i for i in range(1,n+1) if i % 2 != 0]
#     if n % 2 == 0: 
#         # even count = odd count 
#         # even sum > odd sum :: decrease even sum
#         # do (n//2) swaps
#         # first (n//2) even numbers and then remaining odd 
#         # first (n//2) odd numbers and then remaining even 
#         # take first (n//2) numbers from even and swap with odd 
#         for i in range(0, n//4):
#             even[i], odd[i] = odd[i], even[i]
#     else:
#         # odd count > even count 
#         # odd sum > even sum 
#         # swap from odd to even, if only odd_value > even_value
#         # this will be true for everything except 1 
#         for i in range(1, (len(odd)//2) + 1):
#             even[i-1], odd[i] = odd[i], even[i-1]
#     print(len(even))
#     print(" ".join(list(map(str, even))))
#     print(len(odd))
#     print(" ".join(list(map(str, odd))))
# else:
#     print("NO")

# take half sum, remove max from that, keep doing it until you can remove valuse
# if you can't remove a value exactly, put it in another list.  

n = int(input())
s = (n * (n + 1)) // 2
if s % 2 == 0 :
    print("YES")
    half_sum =  s // 2
    la = []
    lac = 0
    lb = []
    lab = 0
    for i in range(n, 0, -1):
        if half_sum >= i:
            la.append(i)
            lac += 1
            half_sum -= i 
        else:
            lb.append(i)
            lab += 1
    print(lac)
    print(" ".join(list(map(str, la))))
    print(lab)
    print(" ".join(list(map(str, lb))))
else:
    print("NO")