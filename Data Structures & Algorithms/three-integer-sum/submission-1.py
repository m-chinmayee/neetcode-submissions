class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] > - n:
                    k -= 1
                elif nums[j] + nums[k] < - n:
                    j += 1
                else:
                    res.append([n, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
    
        return res
                