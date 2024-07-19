class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum_=0
        sum_+=numBottles
        while(numBottles>=numExchange):
            sum_+=numBottles//numExchange
            numBottles=(numBottles%numExchange)+(numBottles//numExchange)
            print(numBottles)
        return sum_



        
