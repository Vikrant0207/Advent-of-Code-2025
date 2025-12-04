with open("Day 4/input.txt", "r") as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]
rows = len(grid)
cols = len(grid[0])

def count_neighbors(i, j):
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
                count += 1
    return count

total_removed = 0

while True:
    remove = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@' and count_neighbors(i, j) < 4:
                remove.append((i, j))
    
    if not remove:
        break
    
    for i, j in remove:
        grid[i][j] = '.'
        total_removed += 1

print(total_removed)
