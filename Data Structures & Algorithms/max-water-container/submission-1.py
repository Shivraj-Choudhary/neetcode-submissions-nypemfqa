class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        i, j = 0, n-1
        while i < j:
            res = max(res, min(heights[i], heights[j]) * (j-i))
            if (heights[i] < heights[j]):
                i += 1
                temp = min(heights[i], heights[j]) * (j-i)
            else:
                j -= 1
                temp = min(heights[i], heights[j]) * (j-i)
            res = max(res, temp)
        return res