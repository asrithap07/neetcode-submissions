class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0, 1
        maxP = 0
        #while s < length
        while s < len(prices):
            #if buy prices is greater than sell price
            if prices[b] >= prices[s]:
                #our window is invalid and we need to move the buy pointer
                b = s
            #if sell price is greater than buy 
            else:
                #save this profit result if its max
                currP = prices[s] - prices[b]
                maxP = max(currP, maxP)
                #move the sell pinter to keepp finding better oftion
            s += 1
        #return largest profit
        return maxP