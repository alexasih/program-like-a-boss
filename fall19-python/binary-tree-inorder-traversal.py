# RECURSIVE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root == None:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
# ITERATIVE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root == None:
            return []
        
        stack = []
        ret = []
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            
            else:
                node = stack.pop()
                ret.append(node.val)
                
                root = node.right
        return ret

        
