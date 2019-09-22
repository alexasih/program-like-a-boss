# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        stack1 = []
        stack2 = []
        ret_stack = []
        num1 = ''
        num2 = ''
        total = ''
        
        head = ListNode(0)
        curr = head
        
        while l1:
            stack1.append(str(l1.val))
            l1 = l1.next
        while l2:
            stack2.append(str(l2.val))
            l2 = l2.next
        
        while stack1:
            num1 += stack1.pop()
            
        while stack2:
            num2 += stack2.pop()
        
        total = str(int(num1) + int(num2))
        
        for digit in total:
            ret_stack.append(digit)
        
        while ret_stack:
            value = int(ret_stack.pop())
            curr.next = ListNode(value)
            curr = curr.next
        
        return head.next
