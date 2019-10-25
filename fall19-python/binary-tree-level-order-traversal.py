# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # adding root node to queue
        queue = [root]
        
        # initialize ret, our return list
        ret=[]
        
        # while root is not None AND queue is not empty []
        # cannot be 'or' because then root can be empty but it still
        # tries to execute -> error
        
        # if we want to just do while queue is not Empty,
        # we need a case in the beginning for if root is None return []
        # before loop executes
        while root and queue:
            
            # current stores the current values of nodes at current level
            current = []
            # nextLevel stores the next nodes
            nextLevel = []
            
            for node in queue:
                
                # add all node values in queue to current
                # whatever is in queue is all the node values
                # for current level of tree
                # but need to keep track of all the current vals
                # and add it to another list that we will add
                # to ret list, so we use 'current'
                current.append(node.val)
            
                # add to queue only if value is not Null/None
                if node.left is not None:
                    nextLevel.append(node.left)
                    # add to a different list, nextLevel
                    # we are adding the NODES not the VALUES
                    # if there are children aka the next level

                # add to queue only if value is not Null/None
                if node.right is not None:
                    nextLevel.append(node.right)
                    # add to a different list, nextLevel
                    # we are adding the NODES not the VALUES
                    # if there are children aka the next level
            
            # append current to ret, and we are done with this
            # level of the tree
            ret.append(current)
            # we are done with this level, so we want the nextLevel,
            # which has the nodes of the children of the current level
            queue = nextLevel
        
        return ret
