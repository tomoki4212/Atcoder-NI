import math

N, L = map(int, input().split())
ans = 1
mod = 10**9 + 7
n = N // L
for s in range(1, n+1):
    # L段がs回登場する場合を考える
    u = N - L*s
    l_s = math.comb((s+u), s)
    ans += l_s
answer = ans % mod
print(answer)
