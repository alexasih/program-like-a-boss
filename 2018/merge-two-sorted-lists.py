# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        curr = head
        
        if (l1 is None and l2):
            return l2
        elif (l1 and l2 is None):
            return l1
        elif (l1 is None and l2 is None):
            return None
        
        while (l1 and l2):
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l2 is not None:
            curr.next = l2
        else:
            curr.next = l1
        
        return head.next
