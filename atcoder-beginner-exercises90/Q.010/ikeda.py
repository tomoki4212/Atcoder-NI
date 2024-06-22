"""
下記のコードだと、どうしても処理時間が超えてしまった
調べたところ、辞書の取り出しにめちゃ時間かかっているようなので、全てリストにしようと思う
"""
# N:生徒の人数
N = int(input()) 
class_1_dict = {}
class_2_dict = {}

for num in range(1, N+1):
    """
    C: クラス名
    P: 点数
    """
    C, P = map(int, input().split())
    if C==1:
        class_1_dict[num] = P
    else:
        class_2_dict[num] = P

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
        a = class_1_dict.get(n)
        if a is not None:
            answer1 += a
        else:
            answer2 += class_2_dict[n]
    print(f"{answer1} {answer2}")


"""
全部リストにしても処理時間が超えてしまった
どうしよう・・・
"""

# N:生徒の人数
N = int(input()) 
class_point_list = [0] * (N+1)

for num in range(1, N+1):
    """
    num: 出席番号(インデックスにしている)
    C: クラス名
    P: 点数
    class_point_list: [0, [class, point], [class, point]・・・]
    """
    C, P = map(int, input().split())
    class_point_list[num] = [C, P]

# Q:問題数
Q = int(input())

for _ in range(Q):
    """
    L: 学籍番号の始まりの番号
    R: 終わりの番号
    """
    # 問題ごとにリセット
    answer1 = 0
    answer2 = 0
    L, R = map(int, input().split())
    for n in range(L, R+1):
        """
        n: 出席番号
        """
        c_p = class_point_list[n]
        your_class = c_p[0]
        point = c_p[1]
        if your_class == 1:
            answer1 += point
        else:
            answer2 += point
    print(f"{answer1} {answer2}")
