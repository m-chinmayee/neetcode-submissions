class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i, n in enumerate(nums):
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
            
            if count[n] > len(nums) / 2:
                return n