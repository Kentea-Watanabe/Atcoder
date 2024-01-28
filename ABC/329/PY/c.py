N = int(input())
A = list(map(int, input().split()))

from itertools import groupby


ans = [(k, len(list(g))) for k,g in groupby(strings)]
print(ans)
#[('a', 2), ('b', 12), ('a', 1)]