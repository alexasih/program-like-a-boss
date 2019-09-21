# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # curr is the current node you are at
        curr = head
        # prev is the reversed linkedlist
        prev= None
        
        # while your current value is not None, then there are still ListNodes to traverse
        while (curr != None):
            
            # continue to traverse with nxt being set to next node
            nxt = curr.next 
            # current is the node you are at right now. 
            # flips order so pointer to next points to the previous element, reversing the linkedlist
            curr.next = prev
            # prev becomes curr, so you can keep track of every node that comes right before current node
            prev = curr
            # set current node equal to next to traverse the linkedlist
            curr = nxt
        
        # we return prev because this is the new head of the reversed linked list
        return prev
        
        
        
        
