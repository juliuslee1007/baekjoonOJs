mtx = []
biggest = 0
index1 = 0
index2 = 0
for i in range(9):
    mtx.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if mtx[i][j] >= biggest:
            index1, index2 = i +1, j + 1
            biggest = mtx[i][j]
print(biggest)
print(index1, index2)