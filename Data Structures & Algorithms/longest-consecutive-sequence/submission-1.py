class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums = sorted(nums)
        l = len(nums)
        count = [1]

        for i in range(l-1):
            diff = nums[i+1] - nums[i]
            if diff == 1:
                count[-1] += 1
            elif diff == 0:
                continue
            else:
                count.append(1)
        
        return max(count)