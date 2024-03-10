from collections import defaultdict

def solve(points):
    m = defaultdict(set)
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if i != j:
                p1 = tuple(points[i])
                p2 = tuple(points[j])
                if p2[0]==p1[0]:
                    m[float("inf")].add(p1)
                    m[float("inf")].add(p2)
                else:
                    slope = (p2[1]-p1[1]) / (p2[0]-p1[0])
                    m[slope].add(p1)
                    m[slope].add(p2)
    print(m)
    max_value = 0
    for slope, ps in m.items():
        if len(ps) > max_value:
            max_value = len(ps)
    return max_value


points = [[3,3],[1,4],[1,1],[2,1],[2,2]]
print(solve(points))