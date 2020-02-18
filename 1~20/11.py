class Solution:
    def maxArea(self, height):
        n = len(height)
        max_vol = 0
        left = 0
        right = n - 1
        while left < right:
            vol = (right - left) * min(height[left], height[right])
            if vol > max_vol:
                max_vol = vol
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_vol
