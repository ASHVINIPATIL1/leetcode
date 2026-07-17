class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        highestProfit = 0
        
        for price in prices:
            
            if price < minPrice:
                minPrice = price

            profit = price - minPrice

            if profit > highestProfit:
                highestProfit = profit

        return highestProfit


        

                
                
                 