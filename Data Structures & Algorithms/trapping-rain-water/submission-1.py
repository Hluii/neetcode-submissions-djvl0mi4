class Solution:
    def trap(self, height: List[int]) -> int:
        # USE TWO POINTERS
        # left until elft is greater and then vice versa
        # add the max - height
        res = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                maxLeft = max(height[left],maxLeft)
                res += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(height[right], maxRight)
                res += maxRight - height[right]
        return res
                
