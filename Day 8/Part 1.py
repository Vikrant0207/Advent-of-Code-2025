import itertools
from collections import Counter

points = []
with open('Day 8/input.txt', 'r') as f:
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

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        parent[px] = py

for dist_sq, i, j in edges[:1000]:
    union(i, j)

components = Counter(find(i) for i in range(n))
sizes = sorted(components.values(), reverse=True)

result = sizes[0] * sizes[1] * sizes[2]
print(result)
