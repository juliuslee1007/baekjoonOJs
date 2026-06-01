def solution(nums : list) -> int:
    return len(nums) // 2 if len(set(nums)) > len(nums) // 2 else len(set(nums))