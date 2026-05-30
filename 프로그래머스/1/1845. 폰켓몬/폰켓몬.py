def solution(nums):
    count = {}
    for p in nums:
        if p in count:
            count[p] += 1
        else:
            count.update({p : 1})
    if len(count) > len(nums) // 2:
         return len(nums) // 2
    else:
        return len(count)