# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(0)
        ret = head
        
        curr_l1 = l1
        curr_l2 = l2
        
        if (curr_l1 is None and curr_l2 is None):
            return None
        
        if (curr_l1 is None and curr_l2):
            return curr_l2
        
        if (curr_l1 and curr_l2 is None):
            return curr_l1
        
        while (curr_l1 and curr_l2):
            if curr_l1.val < curr_l2.val:
                ret.next = curr_l1
                curr_l1 = curr_l1.next
            else:
                ret.next = curr_l2
                curr_l2 = curr_l2.next
            # need to have ret point to the next node so it doesn't keep replacing the same node over and over again
            ret = ret.next
        
        if curr_l1 is not None:
            ret.next = curr_l1
            
        if curr_l2 is not None:
            ret.next = curr_l2
        
        # return head.next NOT ret, because ret is the pointer to current node
        # so it points to last node after iterating over entire linked List
        return head.next
