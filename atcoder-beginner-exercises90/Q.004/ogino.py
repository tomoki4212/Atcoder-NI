import numpy as np

# 行列のサイズを入力
h, w = map(int, input().split())

# 行列を入力
matrix = []
for _ in range(h):
    matrix.append(list(map(int, input().split())))

# 行列をnumpy配列に変換
matrix = np.array(matrix)

# 行の合計と列の合計を計算
row_sum = matrix.sum(axis=1).reshape(-1, 1)  # 行の合計
col_sum = matrix.sum(axis=0).reshape(1, -1)  # 列の合計

# 答えを計算
answer = row_sum + col_sum - matrix

# 答えを出力
for sublist in answer:
    print(*sublist)