class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer 
        highest = 0
        # area = (right-left) * min(heights[right], heights[left])
        left, right = 0, len(heights)-1
        for left, n in enumerate(heights):
            for right in range(len(heights)-1, left, -1):
                area = (right-left) * min(heights[right], heights[left])
                if area > highest:
                    highest = area
                    print("area " + str(area))
                print("highest: " + str(highest))
        return highest
            
            
        