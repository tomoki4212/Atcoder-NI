mod = 10**9 + 7

N = int(input())
# (1+2+3)*(4+5+6)のように一度それぞれのサイコロの和を先に求める
a_list = [list(map(int, input().split())) for _ in range(N)]
sum_list = [sum(a_list[i]) for i in range(N)]

result = 1
for s in sum_list:
    result = (result * s) % mod

print(result)
