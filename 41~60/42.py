class Solution:
    def trap(self, height):
        sum = 0
        max_left = 0    # maximum height to the left of the current left position
        max_right = 0   # maximum height to the right of the current right position
        left = 1        # current left position
        right = len(height) - 2     # current right position
        for i in range(1, len(height) - 1):
            if height[left - 1] < height[right + 1]:
                # max_left < max_right
                # update from left to right
                max_left = max(max_left, height[left - 1])
                if max_left > height[left]:
                    # current left position is shorter
                    sum += max_left - height[left]
                left += 1
            else:
                # max_left > max_right
                # update from right to left
                max_right = max(max_right, height[right + 1])
                if max_right > height[right]:
                    # current right position is shorter
                    sum += max_right - height[right]
                right -= 1

        return sum
