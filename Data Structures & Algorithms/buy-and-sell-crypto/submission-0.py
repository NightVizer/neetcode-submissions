class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        postfix = []
        for indx in range(len(prices)-1, -1, -1):
            postfix.append(max_value)
            
            max_value = max(max_value, prices[indx])
        
        postfix.reverse()

        max_profit = 0
        for indx in range(len(prices)):
            max_profit = max(postfix[indx] - prices[indx], max_profit)

        return max_profit