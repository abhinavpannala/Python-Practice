class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j=0
        total=0
        for i in range(1,len(prices)):
            if prices[j]<prices[i]:
                total+=prices[i]-prices[j]
            j=j+1
        return total
            
                
                
        