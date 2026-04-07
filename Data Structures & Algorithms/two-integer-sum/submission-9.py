class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            target -= nums[i]
            if target in nums[i+1:]:
                check = nums.index(target,i)
                print(nums.index(target,i))
                if check == i:
                    check = nums.index(target,i+1)
                    print("equals")
                return [i,check]
            target += nums[i]


        