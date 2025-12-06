from functools import reduce
from operator import mul

F="Day 6/input.txt"
L=[l.rstrip("\n") for l in open(F)]
op_row = max(i for i,l in enumerate(L) if '+' in l or '*' in l)
L = L[:op_row+1]
W = max(len(x) for x in L)
G = [x.ljust(W) for x in L]

cols = [ ''.join(G[r][c] for r in range(len(G))) for c in range(W) ]
is_sep = [all(ch==' ' for ch in col) for col in cols]

i=0; grand=0
while i<W:
    if is_sep[i]:
        i+=1; continue
    j=i
    while j<W and not is_sep[j]: j+=1
    rows = [ ''.join(G[r][i:j]).strip() for r in range(len(G)) ]
    nums = []
    for r in range(op_row):
        if rows[r]:
            nums += [int(t) for t in rows[r].split()]
    op = next((ch for ch in rows[op_row] if ch in '+*'), None)
    if op == '+':
        grand += sum(nums)
    else:
        grand += reduce(mul, nums, 1) if nums else 0
    i=j

print(grand)
