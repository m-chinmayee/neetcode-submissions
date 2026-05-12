class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        couple = {}
        for i, n in enumerate(nums):
            m = target - n
            if n not in couple:
                couple[m] = i
            else:
                return sorted([i, couple[n]])