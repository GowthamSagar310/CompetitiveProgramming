import math
t, sx, sy, ex, ey = list(map(int, input().split()))
directions = input()

time = 0

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

current_distance = distance(sx, sy, ex, ey)
for direction in directions:
    if direction == "N":
        new_distance = distance(sx, sy+1, ex, ey)
        if new_distance < current_distance:
            sy = sy + 1
            current_distance = new_distance
    if direction == "S":
        new_distance = distance(sx, sy-1, ex, ey)
        if new_distance < current_distance:
            sy = sy - 1
            current_distance = new_distance
    if direction == "E":
        new_distance = distance(sx+1, sy, ex, ey)
        if new_distance < current_distance:
            sx = sx + 1
            current_distance = new_distance
    if direction == "W":
        new_distance = distance(sx-1, sy, ex, ey)
        if new_distance < current_distance:
            sx = sx -1 
            current_distance = new_distance
    time += 1
    if current_distance == 0: break

print(-1 if current_distance != 0 else time)