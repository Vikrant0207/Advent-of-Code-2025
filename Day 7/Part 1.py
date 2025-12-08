from collections import deque

grid = [line.strip() for line in open("Day 7/input.txt") if line.strip()]
H, W = len(grid), len(grid[0])

for r in range(H):
    for c in range(W):
        if grid[r][c] == 'S':
            start = (r, c)

queue = deque([start])
visited = set()
splits = 0

while queue:
    r, c = queue.popleft()
    if (r, c) in visited:
        continue
    visited.add((r, c))

    nr = r + 1
    if nr >= H:
        continue

    cell = grid[nr][c]

    if cell == '^':
        splits += 1
        if c > 0:
            queue.append((nr, c - 1))
        if c < W - 1:
            queue.append((nr, c + 1))
    elif cell == '.':
        queue.append((nr, c))

print(splits)
