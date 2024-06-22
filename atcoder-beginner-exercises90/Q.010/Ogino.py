N = int(input())

C_P = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())

L_R = [list(map(int, input().split())) for _ in range(Q)]

cum_sum_1 = [0] * (N + 1)
cum_sum_2 = [0] * (N + 1)

for i in range(N):
    if C_P[i][0] == 1:
        cum_sum_1[i + 1] = cum_sum_1[i] + C_P[i][1]
        cum_sum_2[i + 1] = cum_sum_2[i]
    else:
        cum_sum_1[i + 1] = cum_sum_1[i]
        cum_sum_2[i + 1] = cum_sum_2[i] + C_P[i][1]

for i in range(Q):
    L, R = L_R[i]
    sum_1 = cum_sum_1[R] - cum_sum_1[L - 1]
    sum_2 = cum_sum_2[R] - cum_sum_2[L - 1]
    print(sum_1, sum_2)
