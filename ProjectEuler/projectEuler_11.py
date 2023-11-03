# n = int(input())
# i = 3
# s = 0
# while ( i < n ):
#     if (i % 3 == 0 or i % 5 == 0):
#         s+= i
#     i+=1
# print(s)
# O(n)


n = int(input())

num_multiples_3 = ((n-1) // 3)
num_multiples_5 = ((n-1) // 5)

s3 = 3 * (((num_multiples_3) * (num_multiples_3 + 1)) // 2)
s5 = 5 * (((num_multiples_5) * (num_multiples_5 + 1)) // 2)

# but we will be count 15, 30,.. (which are 15 multiples) twice 

num_multiples_15 = ((n-1) // 15)
s15 = 15 * (((num_multiples_15) * (num_multiples_15 + 1)) // 2)
print(s3 + s5 - s15)
# O(1)
