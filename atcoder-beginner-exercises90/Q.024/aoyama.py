n,k = map(int,input().split())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

dif_list = []
#AとBのi番目の要素の差の絶対値を取得
for i in range(n): 
    dif_list.append(abs(a_list[i]-b_list[i]))

#差の絶対値の合計を取得
sum =sum(dif_list)

#差の絶対値の合計がk以下、かつ偶奇が一致していればOK
if sum <= k:
    if sum % 2 == k % 2:
        print("Yes")
        exit()
print("No")