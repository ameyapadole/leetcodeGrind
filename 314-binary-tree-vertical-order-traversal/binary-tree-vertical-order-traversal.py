# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        columnTable = defaultdict(list)
        min_col = max_col = 0 

        while q: 
            node, cols = q.popleft()
            if node: 
                columnTable[cols].append(node.val)
                q.append((node.left, cols - 1))
                q.append((node.right, cols + 1))

                min_col = min(min_col, cols)
                max_col = max(max_col, cols)
        return [columnTable[i] for i in range(min_col, max_col + 1)]