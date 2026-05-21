class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        for i, m in enumerate(nums):
            total = 1
            for j, n in enumerate(nums):
                if j != i:
                    total *= n
            res[i] = total
        
        return res