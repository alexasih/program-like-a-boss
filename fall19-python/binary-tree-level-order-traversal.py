# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        queue = [root]
        ret = []
        
        while queue:
            temp = []
            new_queue = []
            for node in queue:
                temp.append(node.val)
                
                if node.left:
                    new_queue.append(node.left)
                    
                if node.right:
                    new_queue.append(node.right)
                
            
            queue = new_queue
            
            ret.append(temp)
            
        
        return ret
