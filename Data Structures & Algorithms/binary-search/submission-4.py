class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, mid, right = 0, len(nums)//2, len(nums)-1
        if target < nums[0] or target > nums[len(nums)-1]:
            print(str(nums[0]) + str(nums[len(nums)-1]) )
            return -1
        if len(nums) < 3:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
        while mid != left and mid != right:
            print("mid: " + str(mid))
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] > target:
                right = mid
                mid = ((right - left)//2) + left
            if nums[mid] < target:
                left = mid
                mid = ((right - left)//2) + left
        return -1
            