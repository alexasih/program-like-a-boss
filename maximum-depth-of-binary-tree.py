# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        queue = [root]
        ret = []
        
        while root and queue:
            
            current = []
            nextLevel = []
            
            for node in queue:
                current.append(node.val)
                
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            ret.append(current)
            
            queue = nextLevel
        
        return len(ret)
        
        
        
        
