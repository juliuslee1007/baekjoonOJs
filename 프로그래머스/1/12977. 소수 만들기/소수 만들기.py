from itertools import combinations as comb
import math as m

def is_prime(n):
    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    p_c = list(comb(nums, 3))
    ans = 0
    for p in p_c:
        if is_prime(sum(p)):
            ans += 1
    return ans