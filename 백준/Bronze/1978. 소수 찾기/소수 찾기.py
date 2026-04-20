
import math

result = 0
chk = 0
re = int(input())
nums = list(map(int, input().split()))
for i in range(re):
    n = nums[i]
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            chk += 1
    if chk == 0 and n != 1:
        result += 1
    chk = 0
print(result)