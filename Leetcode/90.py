res = []

def recur(index, n, arr, ds, res):
    res.append(ds[:])
    for i in range(index, n):
        if i > index and arr[i] == arr[i-1]: continue
        ds.append(arr[i])
        recur(i+1, n, arr, ds, res)
        ds.pop()

arr = [1,2,2]
arr.sort()
recur(0, len(arr), arr, [], res)
print(res)