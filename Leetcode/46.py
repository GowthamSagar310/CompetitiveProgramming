arr = [1, 2, 3]

def recur(cindexes, n, arr, ds, res):

    if len(ds) == n:
        res.append(ds[:])
        return

    for i in range(n):
        if i not in cindexes:
            cindexes.append(i)
            ds.append(arr[i])
            recur(cindexes, n, arr, ds, res)
            ds.pop()
            cindexes.pop()

# instead of storing indexes in a list, use a boolean array for better complexity. 

def recur2(map, n, arr, ds, res):
    if len(ds) == n:
        res.append(ds[:])
        return 
    
    for i in range(n):
        if not map[i]:
            map[i] = True
            ds.append(arr[i])
            recur(map, n, arr, ds, res)
            map[i] = False
            ds.pop()

def swapping_solution(index, n, arr, res):

    if index == n:
        res.append(arr[:])
        return 
    
    for i in range(index, n):
        arr[index], arr[i] = arr[i], arr[index]
        swapping_solution(index+1, n, arr, res)
        arr[index], arr[i] = arr[i], arr[index]

res = []
swapping_solution(0, len(arr), arr, res)
print(res)