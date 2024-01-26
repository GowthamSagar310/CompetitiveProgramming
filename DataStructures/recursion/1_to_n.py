# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?category=

def recur(n):
    if n <= 0: return
    recur(n-1)
    print(n, end=" ")

recur(6)