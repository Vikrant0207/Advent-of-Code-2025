with open("Day 4/input.txt", "r") as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]
rows = len(grid)
cols = len(grid[0])

count = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '@':
            neighbor_count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
                        neighbor_count += 1
            if neighbor_count < 4:
                count += 1

print(count)
