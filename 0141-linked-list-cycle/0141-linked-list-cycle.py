# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list1 = {}
        temp = head
        while temp:
            if temp.next in list1:
                return True
            list1[temp.next]=True
            temp = temp.next
        return False

        