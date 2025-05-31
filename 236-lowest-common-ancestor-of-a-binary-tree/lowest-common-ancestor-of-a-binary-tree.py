# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root  # Base case: if root is None or matches p/q
        
        left = self.lowestCommonAncestor(root.left, p, q)  # Recur for left subtree
        right = self.lowestCommonAncestor(root.right, p, q)  # Recur for right subtree
        
        if left and right:  # If p and q found in different subtrees, return root
            return root
        
        return left or right  # Return non-None value (either left or right)
