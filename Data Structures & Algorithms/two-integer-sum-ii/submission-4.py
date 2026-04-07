class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fast, slow = 1,0
        while slow < len(numbers): 
            fast = slow
            while fast < len(numbers):
                
                curr_sum = numbers[fast] + numbers[slow]
                print("curr_sum: " + str(curr_sum))
                if target == curr_sum:
                    return [slow+1, fast+1]
                print("fast: " + str(fast))
                fast += 1
            print("slow: " + str(slow))
            slow += 1
        return [slow+1,fast+1]

