
# did not solve

pages = int(input())
arr = list(map(int, input().split()))

def count(pages, arr):

    day = 1
    while pages > 0:
        pages -= arr[day-1] 
        if pages <= 0: return day 
        day += 1
        if day > 7: day = 1
    return day


print(count(pages, arr))
