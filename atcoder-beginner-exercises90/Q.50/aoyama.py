n, l = map(int,input().split())

if n < l:
  print(1)
  exit()
  
ways = [1] * (n+1)
ways[0] = 0
ways[l] = 2

for i in range(l+1,n+1):
    ways[i] = ways[i-1] + ways[n]

print(ways[-1]%(10**9+7))