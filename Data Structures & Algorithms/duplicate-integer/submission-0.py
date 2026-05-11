class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for i, num in enumerate(nums):
            if num not in unique:
                unique.append(num)
            else:
                return True
        return False