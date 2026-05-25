import sys
sys.setrecursionlimit(10**6)

arr = [-1] * 100001
arr[0] = 0
arr[1] = 1
def solution(n):
    if arr[n] != -1:
        return arr[n]
    arr[n] = solution(n - 1) + solution(n - 2)
    return arr[n] % 1234567
    