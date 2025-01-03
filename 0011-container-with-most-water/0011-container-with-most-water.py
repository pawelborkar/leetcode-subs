class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            # At each iteration calculate the result befor moving the pointers

            res = max(res, min(height[right], height[left]) * (right - left))

            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1
        return res