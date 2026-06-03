class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        vol = 0

        for i, n in enumerate(heights):
            j = len(heights) - 1
            while j > i:
                if ((j - i) * min(heights[i], heights[j])) > vol:
                    vol = (j - i) * min(heights[i], heights[j])
                j -= 1
        return vol