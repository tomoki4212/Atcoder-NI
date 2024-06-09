# N:生徒の人数
N = int(input()) 
class_point_list = [0] * (N+1)

for num in range(1, N+1):
    """
    num: 出席番号
    C: クラス名
    P: 点数
    """
    C, P = map(int, input().split())
    class_point_list[num] = [C, P]

print(class_point_list)

# Q:問題数
Q = int(input())

for _ in range(Q):
    """
    L: 学籍番号の始まりの番号
    R: 終わりの番号
    """
    # リスト内を問題ごとにリセット
    answer1 = 0
    answer2 = 0
    L, R = map(int, input().split())
    for n in range(L, R+1):
        c_p = class_point_list[n]
        your_class = c_p[0]
        point = c_p[1]
        if your_class == 1:
            answer1 += point
        else:
            answer2 += point
    print(f"{answer1} {answer2}")


"""
上記のコードだと、どうしても処理時間が超えてしまった
調べたところ、辞書の取り出しにめちゃ時間かかっているようなので、全てリストにしようと思う
"""
