# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([(root, 0)])
        columnTable = collections.defaultdict(list)
        min_cols = max_cols = 0

        if not root:
            return []

        while queue: 
            node, col = queue.popleft()
            if node is not None:
                columnTable[col].append(node.val)
                min_cols = min(min_cols, col)
                max_cols = max(max_cols, col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        return [columnTable[x] for x in range(min_cols, max_cols + 1)]

        