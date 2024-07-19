class Solution(object):

    def check_x(self,i,j,k,arr):
        if arr[i]^arr[j]==arr[k]:
            return True
        elif arr[j]^arr[k]==arr[i]:
            return True
        elif arr[i]^arr[k]==arr[j]:
            return True
        else:
            return False
    
    def countTriplets(self, arr):
        
        ind_count=0

        a=0

        for i in range(len(arr)):
            a=arr[i]
            for j in range(i+1,len(arr)):
                a^=arr[j]
                if a==0:
                    ind_count+=j-i
        return ind_count
