class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([(root, 0)])
        column_table = collections.defaultdict(list)
        min_cols = max_cols = 0 

        if not root: 
            return []

        while queue:
            node, cols = queue.popleft()
            if node is not None:
                column_table[cols].append(node.val)

                min_cols = min(cols, min_cols)
                max_cols = max(cols, max_cols)

                queue.append((node.left, cols - 1))
                queue.append((node.right, cols + 1))
        return [column_table[i] for i in range(min_cols, max_cols + 1)]
        