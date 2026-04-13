N, M = map(int, input().split())
mtx1 = []
mtx2 = []
result = []
for i in range(N):
    mtx1.append(list(map(int, input().split())))
for i in range(N):
    mtx2.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        result.append(mtx1[i][j] + mtx2[i][j])

for i in range(N):
    print(*result[M * i:M * i + M])
    