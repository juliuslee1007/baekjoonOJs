from itertools import permutations as p
import math as m

def is_prime(n : int) -> bool:
    if n == 0 or n == 1:
        return False
    for i in range(2, int(m.sqrt(n)) + 1):    
        if n % i == 0:
            return False
    return True

def solution(numbers):
    arr = list(numbers)
    nums = set()
    for i in range(1, len(arr) + 1):
        perms = p(arr, i)
        for a in perms:
            if is_prime(int(''.join(a))):
                nums.add(int(''.join(a)))
    answer = len(nums)
    return answer