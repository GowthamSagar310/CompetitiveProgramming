n = int(input())
arr = list(map(int, input().split()))

# brute force  O(n * logn) + O(n) --> O(n *logn)
# 1. put all elements in a set --> O(n * logn)
# 2. take length of set
# 3. put all those elements of the set back into the arr --> O(n) 
# space complexity : O(n) (set size in worst case)


# optimal approach O(n) and in-place 
def remove_duplicates(arr, n):
    pointer1 = 0
    pointer2 = 1
    while pointer2 < n and pointer1 < n:
        if arr[pointer1] != arr[pointer2]:
            pointer1 += 1
            arr[pointer1] = arr[pointer2]
            pointer2 += 1
        else:
            pointer2 += 1
    return arr[:pointer1+1]

print(remove_duplicates(arr, n))