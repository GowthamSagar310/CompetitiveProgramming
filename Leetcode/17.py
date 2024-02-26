map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def something(digits, map):
    if not digits: return []
    if len(digits) == 1: return list(map[digits])   
    res = []
    def recur(index, n, letters, ds, res):
        if index >= n: 
            res.append(ds[:])
            return 
        for i in range(len(letters[index])):
            ds += letters[index][i]
            recur(index+1, n, letters, ds, res)
            ds = ds[:-1]
    letters = [map[digit] for digit in digits]
    recur(0, len(digits), letters, "", res)
    return res         

digits = "234"
print(something(digits , map))