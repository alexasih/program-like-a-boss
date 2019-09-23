# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# SOLUTION USING STACKS

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

# SOLUTION WITH ELEMENTARY ADDITION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Test Cases
        # carry over
        # carry over creates an extra line (999+1 = 1000)
        # 98 + 1 = 99
        # 90 + 0 = 90
        # what if one linkedlist is larger than the other? how do you add?
        
        head = ListNode(0)
        curr = head
        
        carry = 0
        while l1 and l2:
            value = l1.val+l2.val+carry
            if value < 10:
                curr.next = ListNode(value)
                if carry == 1:
                    carry = 0
            else:
                value = value-10
                curr.next = ListNode(value)
                carry = 1
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
                
        while l1:
            value = l1.val+carry
            if value < 10:
                curr.next = ListNode(value)
                if carry == 1:
                    carry = 0
            else:
                value = value-10
                curr.next = ListNode(value)
                carry = 1
            curr = curr.next
            l1 = l1.next
            
        while l2:
            value = l2.val+carry
            if value < 10:
                curr.next = ListNode(value)
                if carry == 1:
                    carry = 0
            else:
                value = value-10
                curr.next = ListNode(value)
                carry = 1
            curr = curr.next
            l2 = l2.next
        
        if carry == 1:
            curr.next = ListNode(1)
        
        return head.next
        
