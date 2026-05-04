import math as m

def solution(n):
    arr = [True] * (n + 1)
    arr[0], arr[1] = False, False
    for i in range(2, int(m.sqrt(n)) + 1):
        if arr[i] :
            for j in range(i * 2, n + 1, i):
                arr[j] = False
            
    return arr.count(True)