"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root is None: 
            return []
      
        # Create an empty queue for level order traversal 
        queue = [root]
        ret = []
  
        while(queue): 
            # Print front of queue and remove it from queue 
            temp = []
            new_queue = []
            for node in queue:
                temp.append(node.val)
                
                for child in node.children:
                    new_queue.append(child)
            
            queue = new_queue
            
            ret.append(temp)
            
        return ret
