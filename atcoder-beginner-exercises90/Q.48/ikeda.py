n, k = map(int, input().split())
ten = []
for _ in range(n):
    a, b = map(int, input().split())
    ten.extend([a - b, b])
ten.sort(reverse=True)

print(sum(ten[:k]))
