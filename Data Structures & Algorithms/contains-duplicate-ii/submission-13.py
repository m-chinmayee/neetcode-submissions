class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = {}
        for i, n in enumerate(nums):
            if n not in unique:
                unique[n] = i
            else:
                if abs(i - unique[n]) <= k:
                    return True
                else:
                    unique[n] = i
        return False