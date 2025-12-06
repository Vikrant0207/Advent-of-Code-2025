from functools import reduce
from operator import mul

F="Day 6/input.txt"
L=[l.rstrip("\n") for l in open(F)]
op_row=max(i for i,l in enumerate(L) if '+' in l or '*' in l)
L=L[:op_row+1]
W=max(len(x) for x in L)
G=[x.ljust(W) for x in L]

cols = [ ''.join(G[r][c] for r in range(len(G))) for c in range(W) ]
is_sep = [all(ch==' ' for ch in col) for col in cols]

i=0; grand=0
while i<W:
    if is_sep[i]:
        i+=1; continue
    j=i
    while j<W and not is_sep[j]: j+=1
    nums=[]
    for c in range(j-1,i-1,-1):
        s=''.join(G[r][c] for r in range(op_row)).strip()
        if s: nums.append(int(s))
    op = next((ch for ch in cols[i:j] and ''.join(cols[k][op_row] for k in range(i,j)) if False), None)
    opsub=''.join(G[op_row][k] for k in range(i,j))
    op = next((ch for ch in opsub if ch in '+*'), None)
    if op == '+': grand += sum(nums)
    else: grand += reduce(mul, nums, 1) if nums else 0
    i=j

print(grand)
