def getNum(row,col):
    if row == col:
        return row**2 - (row-1)
    elif row > col:
        mid = row**2 - (row-1)
        if row % 2 != 0: # odd row 
            mid -= (row-col)
        else:
            mid += (row-col)
        return mid 
    else: 
        mid = col**2 - (col-1)
        if col % 2 != 0: # odd row 
            mid += (col-row)
        else:
            mid -= (col-row)
        return mid 

for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    print(getNum(x,y))
               