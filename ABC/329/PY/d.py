import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
idx,val = 0,0
candidate = [0]*(N+1)
ans = ['0']*M
for ix,i in enumerate(A):
    candidate[i] += 1
    if candidate[i] > val: val = candidate[i];idx = i
    elif candidate[i] == val: idx = min(i,idx)
    ans[ix] = str(idx)
print('\n'.join(ans))