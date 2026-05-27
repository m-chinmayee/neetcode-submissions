class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        if nums1[m-1] < nums2[0]:
            nums1[m:] = nums2
            return nums1
        
        i = m - 1
        j = n - 1
        f = m + n - 1
        while j >= 0:
            if nums1[i] >= nums2[j] and i >= 0:
                nums1[f] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j] and i >= 0:
                nums1[f] = nums2[j]
                j -= 1
            elif i < 0:
                nums1[:j+1] = nums2[:j+1]
                return nums1
            f -= 1
        return nums1
        