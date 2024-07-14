h,w = map(int,input().split())
h_2 = h//2 + h % 2
w_2 = w//2 + w % 2
if h >= 2 and w >= 2:
    print(h_2*w_2)
# hかwが1のときは全ての領域にLEDをおける
else:
    print(h*w)