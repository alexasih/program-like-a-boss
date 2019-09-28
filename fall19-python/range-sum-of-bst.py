# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        # test with zeroes
        # Test with negative values
        # test all negative
        # test all positive
        # test both
        
        if root is None:
            return 0
        
        bst_sum = 0
            
        if root.val >= L and root.val <= R:
            bst_sum += root.val
        
        return self.rangeSumBST(root.left,L,R) + bst_sum + self.rangeSumBST(root.right,L,R)
        
