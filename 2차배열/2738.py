N, M = map(int, input().split())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

res = []
for i in range(N):
    row = []
    for j in range(M):
        row_sum = A[i][j] + B[i][j]
        row.append(row_sum)
    res.append(row)

for i in res:
    print(*i)