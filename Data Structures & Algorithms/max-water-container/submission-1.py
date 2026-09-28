class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0
        

        while l < r:
            if heights[l] < heights[r]:
                maxi = heights[l] * (r - l)
                l += 1
            else:
                maxi = heights[r] * (r - l)
                r -= 1
            
            maximum = max(maxi, maximum)
        
        return maximum

        