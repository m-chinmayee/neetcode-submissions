class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        min = 0
        max = len(nums) - 1
        mid = nums[(min + max)//2]
        while min <= max:
            if target < mid:
                max = (min + max)//2 - 1
                mid = nums[(min + max)//2]
            elif target > mid:
                min = (min + max)//2 + 1
                mid = nums[(min + max)//2]
            else:
                return (min + max)//2
        return -1