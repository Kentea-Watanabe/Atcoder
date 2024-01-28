from itertools import groupby
# 入力の最初の行を整数として読み込む
n = int(input())

# 次の行を文字列として読み込む
s = input()


z = [(k, len(list(g))) for k,g in groupby(s)]
# キーごとに最大の値を格納するための辞書
max_values = {}

# 各タプルに対してループ
for key, value in z:
    # キーが辞書にまだ存在しないか、現在の値が以前の値より大きい場合、値を更新
    if key not in max_values or value > max_values[key]:
        max_values[key] = value

# 辞書の値の合計
total = sum(max_values.values())

print(total)