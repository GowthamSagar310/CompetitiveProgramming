res = []
def recur(index, n, arr, target_length, target, ds, res):
    if len(ds) > target_length: return
    if target == 0 and len(ds) == target_length:
        res.append(ds[:]) 
    if index > n: return 
    
    for i in range(index, n):
        if arr[i] > target: break
        ds.append(arr[i])
        recur(i+1, n, arr, target_length, target-arr[i], ds, res)
        ds.pop()
    
length = 9
target = 45
arr = [i for i in range(1, 10)]
recur(0, len(arr), arr, length, target, [], res)
print(res)