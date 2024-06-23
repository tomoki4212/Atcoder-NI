import math

A, B, C = map(int, input().split())
# 最大公約数から考える
ABC_gcd = math.gcd(A, B, C)
# floatにするとオーバーフローを引き起こすため//に
answer = (A//ABC_gcd + B//ABC_gcd + C//ABC_gcd) - 3
print(answer)
print("test")