from collections import defaultdict

with open("Day 7/input.txt", "r") as f:
    grid = [line.strip() for line in f if line.strip()]

rows = len(grid)
cols = len(grid[0])

start_r, start_c = None, None
for i, row in enumerate(grid):
    for j, ch in enumerate(row):
        if ch == 'S':
            start_r, start_c = i, j
            break
    if start_r is not None:
        break

dp = [[0] * cols for _ in range(rows)]
dp[start_r][start_c] = 1

for r in range(start_r, rows - 1):
    for c in range(cols):
        if dp[r][c] > 0:
            nr = r + 1
            ch = grid[nr][c]
            if ch == '.':
                dp[nr][c] += dp[r][c]
            elif ch == '^':
                if c - 1 >= 0:
                    dp[nr][c - 1] += dp[r][c]
                if c + 1 < cols:
                    dp[nr][c + 1] += dp[r][c]

timelines = sum(dp[rows - 1])
print(timelines)
