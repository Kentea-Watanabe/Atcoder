N = input()

# 整数の入力
a = int(input())

# 少数の入力
x = float(input())

# リストとして受け取る
S = input().split()

# 1行に複数の整数
N = int(input())
A = list(map(int, input().split()))

# 1行に決まった数の整数」
a, b = map(int, input().split())


# スペース区切りの整数の入力
b, c = map(int, input().split())

# 複数列の読み込みをリストにしてしまう。
N, M = map(int, input().split())
s = [input() for i in range(N)]
t = set([input() for i in range(M)])

# 最初にすべて読み込む必要がある場合 - 行列、グリッド
H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())


# 文字列の入力
s = input()
# 出力
print("{} {}".format(a + b + c, s))
