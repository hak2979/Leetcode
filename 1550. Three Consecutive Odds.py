class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        o=0
        for i in arr:
            if i%2!=0:
                o+=1
                if o==3:
                    return True
            else:
                o=0
        
        return False
        
