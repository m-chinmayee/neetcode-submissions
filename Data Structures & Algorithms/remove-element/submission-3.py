class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        id = 0
        n = len(nums)
        while id < n:
            if nums[id] != val:
                id += 1
            else:
                n -= 1
                nums[id] = nums[n]
        return n 