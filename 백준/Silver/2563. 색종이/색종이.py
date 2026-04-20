paper = [[0] * 100 for i in range(100)]
num_black = int(input())
for i in range(num_black):
    cor1, cor2 = map(int, input().split())
    for x in range(10):
        for y in range(10):
            paper[cor1 + x][cor2 + y] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)