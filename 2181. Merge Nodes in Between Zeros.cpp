# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tem=head.next
        sumz=0
        x=[]
        while tem!=None:
            if tem.val==0:
                x.append(sumz)
                sumz=0
            else:
                sumz+=tem.val
            tem=tem.next
        head=ListNode(x[0])
        p=head
        x.pop(0)
        for i in x:
            p.next=ListNode(i)
            p=p.next

        return head
        
