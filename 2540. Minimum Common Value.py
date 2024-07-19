class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xs=set(nums1)
        for i in range(len(nums2)):
            if nums2[i] in xs:
                return nums2[i]
        return -1
        
