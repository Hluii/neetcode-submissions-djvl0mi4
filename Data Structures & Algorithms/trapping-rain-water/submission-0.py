class Solution:
    def trap(self, height: List[int]) -> int:
        # Intialize two pointers one at the far left and right
        left, right = 0, len(height)-1
        res = 0
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
        return res