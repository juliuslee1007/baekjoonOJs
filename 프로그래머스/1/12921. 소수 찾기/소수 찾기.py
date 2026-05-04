import math as m

def solution(n):
    p_n = [2]
    for i in range(3, n + 1):
        check = True
        for p in p_n:
            if p > m.sqrt(i):
                break
            if i % p == 0:
                check = False
                break
        if check == True:
            p_n.append(i)
            
    return len(p_n)