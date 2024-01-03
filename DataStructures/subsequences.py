# print all binary strings in lexicographic order of length n 

# n = int(input())
# # there is no reference being passed around
# def function(index, ans, n):
#     if index >= n :
#         print(ans)
#         return
#     if ans and ans[-1] == "1":
#         function(index+1, ans+"0", n)
#     else:
#         function(index+1, ans+"0", n)
#         function(index+1, ans+"1", n)

# function(0, "", n)

# take non-take method
# ds is being passed around as a reference. 
# def take_non_take_function(index, ds, ans, n):
#     if index >= n:
#         ans.append(ds.copy())
#         return
    
#     if ds and ds[-1] == "1":
#         ds.append("0")
#         function(index+1, ds, ans, n)
#         ds.pop()
#     else:
#         ds.append("0")
#         function(index+1, ds, ans, n)
#         ds.pop()
#         ds.append("1")
#         function(index+1, ds, ans, n)
#         ds.pop()
#     return ans

# for a in function(0, [], [], 3):
#     print(a)

# print all subsequences using recursion 

# n = int(input())
# arr = list(map(int, input().split()))

# def sub_sequences(index, ds, ans, n, arr):
#     if index >= n:
#         # if not passed as a reference 
#         # ans.append(ds)
#         ans.append(ds.copy())
#         return
#     # another version can be just to pass as a new list 
#     # sub_sequences(index+1, ds + [arr[index]], ans, n, arr)
#     # sub_sequences(index+1, ds, ans, n, arr)
#     ds.append(arr[index])
#     sub_sequences(index+1, ds, ans,  n, arr)
#     ds.pop()
#     sub_sequences(index+1, ds, ans, n, arr)
#     return ans 

# print(sub_sequences(0, [], [], n, arr))


# print all subsequences with sum k 

# n, k = list(map(int, input().split()))
# arr = list(map(int, input().split()))

# def function(index, ds, ans, s, arr, n, k):
#     # if s == k:
#     #     ans.append(ds.copy())
#     if index >= n:
#         if s == k:
#             ans.append(ds.copy())
#         return 
    
#     ds.append(arr[index])
#     s += arr[index]
#     function(index+1, ds, ans, s, arr, n, k)

#     ds.pop()
#     s -= arr[index]
#     function(index+1, ds, ans, s, arr, n, k)

#     return ans 

# print(function(0, [], [], 0, arr, n, k))

# print only one subsequence with sum k 
# def function(index, ds, ans, s, arr, n, k):
#     if index >= n:
#         if s == k:
#             print(ds)
#             return True
#         return False
    
#     ds.append(arr[index])
#     s += arr[index]
#     if function(index+1, ds, ans, s, arr, n, k):
#         return True

#     ds.pop()
#     s -= arr[index]
#     if function(index+1, ds, ans, s, arr, n, k):
#         return True

#     return False

# function(0, [], [], 0, arr, n, k)


# count all subsequences with sum k

# def function(index, s, arr, n, k):
#     if index >=n:
#         if s == k:
#             return 1
#         return 0  
    
#     s += arr[index]
#     l = function(index+1, s, arr, n, k)
#     s -= arr[index]
#     r = function(index+1, s, arr, n, k)
#     return l+r 

# print(function(0, 0, arr, n, k))


# generate parenthesis 

# def recursive_call(index, ds, s, n, ans):
#     if index == n:
#         if s == 0:
#             ans.append(ds)
#         return 
#     recursive_call(index+1, ds+"(", s+1, n, ans)
#     if s > 0:
#         recursive_call(index+1, ds+")", s-1, n, ans)
#     return ans 

# n = int(input())
# print(recursive_call(0, "", 0, 2*n, []))


# combination sum 1

# n, k = list(map(int, input().split()))
# arr = list(map(int, input().split()))

# def recursive_call(index, ds, ans, target, n, arr):

#     if index >= n:
#         if target == 0:
#             ans.append(ds.copy())
#         return 

#     # move forward with picking
#     if (arr[index] <= target):
#         ds.append(arr[index])
#         recursive_call(index, ds, ans, target-arr[index], n, arr)
#         ds.pop()

#     # move forward without picking
#     recursive_call(index+1, ds, ans, target, n, arr)
#     return ans

# print(recursive_call(0, [], [], k, n, arr))

# combination sum 2 
# unique combinations 
# lexicographic order 
# each number can be used only one --> we always move forward 

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

# s = sorted(list(input()))


# def recursive_call(ds, map, ans, s):

#     if len(ds) == len(s):
#         ans.append("".join(ds.copy()))
#         return
    
#     already_seen = {k:False for k in s}
#     for i in range(len(s)):
#         if not map[i] and not already_seen[s[i]]:
#             already_seen[s[i]] = True
#             map[i] = True
#             ds.append(s[i])
#             l = recursive_call(ds, map, ans, s)
#             ds.pop()
#             map[i] = False
        
#     return ans 

# ans = recursive_call([], [False] * len(s), [],  s)
# print(len(ans))
# for permutation in ans:
#     print(permutation)




