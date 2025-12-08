import itertools

points = []
with open('input.txt', 'r') as f:
    for line in f:
        x, y, z = map(int, line.strip().split(','))
        points.append((x, y, z))

n = len(points)

edges = []
for i, j in itertools.combinations(range(n), 2):
    p1 = points[i]
    p2 = points[j]
    dist_sq = sum((a - b) ** 2 for a, b in zip(p1, p2))
    edges.append((dist_sq, i, j))

edges.sort()

parent = list(range(n))
components = n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        parent[px] = py
        return True 
    return False  

last_edge = None
for dist_sq, i, j in edges:
    if union(i, j):
        components -= 1
        if components == 1:
            last_edge = (i, j)
            break

if last_edge:
    x1 = points[last_edge[0]][0]
    x2 = points[last_edge[1]][0]
    result = x1 * x2
    print(result)
else:
    print("All were already connected, but that shouldn't happen.")
