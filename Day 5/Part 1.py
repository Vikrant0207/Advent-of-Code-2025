with open('Day 5/input.txt') as f:
    lines = f.read().strip().split('\n')

ranges = []
i = 0
while lines[i] != '':
    start, end = map(int, lines[i].split('-'))
    ranges.append((start, end))
    i += 1

i += 1 
ids = [int(line) for line in lines[i:]]

count = 0
for id in ids:
    for start, end in ranges:
        if start <= id <= end:
            count += 1
            break

print(count)