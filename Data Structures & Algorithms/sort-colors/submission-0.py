class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if nums is None:
            return None
        
        if len(nums) == 0 or len(nums) == 1:
            return nums

        r = 0
        w = 0
        b = 0
        for i, n in enumerate(nums):
            if n == 0:
                r += 1
            elif n == 1:
                w += 1
            elif n == 2:
                b += 1
        nums[:r-1] = [0] * r
        nums[r:r+w-1] = [1] * w
        nums[r+w:] = [2] * b