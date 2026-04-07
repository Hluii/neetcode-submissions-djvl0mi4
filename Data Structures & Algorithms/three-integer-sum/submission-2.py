class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        res = []
        nums = sorted(nums)
        # loop through nums
        for i, n in enumerate(nums):
            left, right = i+1, len(nums) - 1
            while left < right:
                sum = n + nums[left] + nums[right]
                print("sum: "+ str(sum))
                if sum == 0:
                    res_list = [n,nums[left],nums[right]]
                    if res_list not in res:
                        res.append(res_list)
                    right -= 1
                if sum > 0: 
                    right -= 1
                if sum < 0:
                    left += 1
            print(res)
        return res
                
            
        # use 2 pointer on nums + 1 and len(nums) -1 to find 0
