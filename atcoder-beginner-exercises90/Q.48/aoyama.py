# 入力
n,k = map(int, input().split())
ab =  [list(map(int,input().split())) for _ in range(n)]

# 一分で得られる最大点数（部分点、満点 - 部分点）が大きい順に並び替える
list = [b for a,b in ab] + [ a-b for a,b in ab]
list.sort(reverse=True)

# k分までで得られる点数を出力
print(sum(list[:k]))