n = int(input())

f = [[float("inf") for _ in range(n)] for __ in range(1<<n)]
w = []

for i in range(n):
  w.append(list(map(int, input().split())))
    
f[1][0] = 0
for i in range(1 << n):
  for j in range(n):
    if i >> j & 1:
      for k in range(n):
        if (i - (1<<j)) >> k & 1:
          # print(i, j)
          f[i][j] = min(f[i][j], f[i - (1 << j)][k] + w[k][j])
print(f[(1<<n)-1][n-1])