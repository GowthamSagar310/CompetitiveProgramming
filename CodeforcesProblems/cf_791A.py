a,b = list(map(int, input().split()))
if a==b: print("1")
else:
    for i in range(1,11):   
        a = a * 3 
        b = b * 2
        if a*i > b*i:
            print(i)
            break
