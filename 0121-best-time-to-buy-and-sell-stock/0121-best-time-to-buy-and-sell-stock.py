class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: in
        """
        buy_mode = True
        sell_mode = False
        profits = [0]
        a = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<a:
                a = prices[i]
            elif prices[i]>a:
                profits.append(prices[i]-a)
        return max(profits)
             
        