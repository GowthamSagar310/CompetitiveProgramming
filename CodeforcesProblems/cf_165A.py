points = []
for _ in range(int(input())):
    x,y = list(map(int, input().split()))
    points.append((x,y))

def has_upper_lower(point, points):
    has_upper = False
    has_lower = False
    for i in range(len(points)):
        x1, y1 = points[i]
        if point[0] ==x1:
            if point[1] > y1:
                has_lower = True
            if point[1] < y1: 
                has_upper = True
    return has_upper and has_lower 

def has_left_right(point, points):
    has_left = False
    has_right = False
    for i in range(len(points)):
        x1, y1 = points[i]
        if point[1] == y1:
            if point[0] < x1:
                has_right = True
            if point[0] > x1:
                has_left = True
    return has_left and has_right

centers = 0 
for i in range(len(points)):
    if has_left_right(points[i], points) and has_upper_lower(points[i], points):
        centers += 1

print(centers)
