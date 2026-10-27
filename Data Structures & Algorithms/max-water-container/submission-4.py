class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        water = [[]]
        maxWater = 0
        while l < r:
            h = min(heights[l], heights[r])
            if h * (r-l) > maxWater:
                maxWater = h * (r - l)
                print(maxWater)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        return maxWater
            
            
