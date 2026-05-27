class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return 1
        
        j = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
            elif nums[i] != nums[i-1]:
                j += 1
                nums[j] = nums[i]
                i += 1

        return j+1