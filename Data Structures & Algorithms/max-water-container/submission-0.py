class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp, rp = 0, len(heights) - 1
        res = 0
        while lp < rp: 
            l, r = heights[lp], heights[rp]
            area = min(l, r) * (rp - lp)
            res = max(area, res)
            if l <= r:
                lp += 1
            else:
                rp -= 1
        return res