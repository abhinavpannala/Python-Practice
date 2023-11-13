# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevnode=head
        currnode=head
        for i in range(n):
            currnode = currnode.next
        if currnode==None:
            return head.next
        while(currnode.next!=None):
            currnode=currnode.next
            prevnode=prevnode.next
        prevnode.next=prevnode.next.next
        return head           