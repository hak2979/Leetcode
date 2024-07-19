class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        total=0
        no_zero=0
        for i in range(len(s)):
            if s[i] == '1':
                total+=1
            else:
                no_zero+=1
        result=""
        while total>1:
            result+='1'
            total-=1
        while no_zero>0:
            result+='0'
            no_zero-=1
        if total>0:
            result+='1'
        return result
