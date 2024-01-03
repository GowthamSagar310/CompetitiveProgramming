# sliding window approach 


n = int(input())
words = list(input().split())
groups = list(map(int, input().split()))



def function(n, words, groups):

    # subsequence 
    # order matters 
    # not need to consecutive 
    if n == 1:
        return [words[0]]
    
    order = [0]
    for i in range(1, n):
        if groups[order[-1]] != groups[i]:
            order.append(i)
    l = []
    for i in order:
        l.append(words[i])
    return l


# def function(n, words, groups):
#     if n == 1:
#         return words[0]
#     left = 0
#     right = 1
    
#     max_left = 0
#     max_right = 1
#     max_diff = right - left 
#     while left < n and right < n:

#         if groups[right-1] != groups[right]:
#             right += 1
#         else:
#             left += 1
#             right += 1
        
#         if max_diff < (right - left):
#             max_left = left 
#             max_right = right 
#             max_diff = right - left

#     l = []
#     for i in range(max_left, max_right):
#         l.append(words[i])
#     return l

print(function(n, words, groups))