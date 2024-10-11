# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        columnTable = defaultdict(list)
        queue = deque([(root, 0)])
        min_column = max_column = 0

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column +1)]
