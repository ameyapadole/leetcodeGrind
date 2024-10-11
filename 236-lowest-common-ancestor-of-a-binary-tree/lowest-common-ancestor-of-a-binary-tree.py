# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recursive_tree(currNode : 'TreeNode'):
            if not currNode:
                return False
            
            left = recursive_tree(currNode.left)
            right = recursive_tree(currNode.right)

            mid = currNode == p or currNode == q

            if mid + left + right >= 2: 
                self.ans = currNode

            return mid or left or right
        recursive_tree(root)
        return self.ans
        