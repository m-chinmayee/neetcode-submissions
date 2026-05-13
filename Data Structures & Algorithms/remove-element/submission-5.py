class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        id = 0
        n = len(nums)
        while id < n:
            if nums[id] == val:
                n -= 1
                nums[id] = nums[n]
            else:
                id += 1
        return n 