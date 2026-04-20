n, f = map(int, input().split())
all_f = []
for i in range(n):
    if n % (i + 1) == 0:
        all_f.append(i + 1)
if len(all_f) < f:
    print(0)
else:
    print(all_f[f - 1])