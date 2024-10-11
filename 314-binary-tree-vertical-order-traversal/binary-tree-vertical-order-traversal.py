# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        queue = deque([(root, 0)])
        columnTable = defaultdict(list) 
        min_cols = max_cols = 0 

        while queue: 
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_cols = min(column, min_cols)
                max_cols = max(column, max_cols)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
        return [columnTable[x] for x in range(min_cols, max_cols + 1)]
        