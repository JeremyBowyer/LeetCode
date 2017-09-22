# https://leetcode.com/problems/trim-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        if root.val < L:
            return trimBST(root.right, L, R)
        
        if root.val > R:
            return trimBST(root.left, L, R)
        
        root.left = trimBST(root.left, L, R)
        root.right = trimBST(root.right, L, R)
        
        return root