class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWidth = float('-inf')
        while(left <= right):
            maxWidth = max(maxWidth, min(height[left], height[right])*(right -left))
            if (height[left] <= height[right]):
                left = left + 1
            else:
                right = right - 1
        return maxWidth