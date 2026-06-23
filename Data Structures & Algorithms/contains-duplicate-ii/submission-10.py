class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums):
            l = len(nums)
        else:
            l = len(nums)-k

        for i in range(l):
            j = i + 1
            while abs(j - i) <= k and j < len(nums):
                if nums[i] == nums[j]:
                    return True
                else:
                    j += 1
        return False