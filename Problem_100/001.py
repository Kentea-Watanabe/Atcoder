while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break

    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            k = x - (i + j)
            print(f'{j} < {k} <= {n}')
            if j < k <= n:
                ans += 1

    print(ans)