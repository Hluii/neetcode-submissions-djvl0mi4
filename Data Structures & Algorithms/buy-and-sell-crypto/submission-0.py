class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # when new left is smaller than current left 
        # change to the smallest first left, keep track of max 
        # then hold the max profit until end of loop and return
        left, right = 0, 1
        if len(prices) < 2:
            return 0
        if len(prices) < 3:
            return max(0, prices[1] - prices[0])
        max_profit, smallest_l = 0, 0
        
        while right <= len(prices) - 1:
            curr_profit = prices[right] - prices[left]
            if curr_profit > max_profit:
                max_profit = curr_profit
            if prices[right] < prices[left]:
                left = right
            right += 1
            print("curr " + str(curr_profit) + " left: " + str(left) + " right: " + str(right) )
        return max_profit
            


