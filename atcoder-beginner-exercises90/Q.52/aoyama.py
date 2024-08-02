import math

n = int(input())
a = [map(int, input().split()) for _ in range(n)]
Q = 10**9+7

sum_dice = list()

for i in range(n):
    sum_dice.append(sum(a[i]))

print(math.prod(sum_dice)%Q)