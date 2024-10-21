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

        if root is None:
            return []
        
        while queue: 
            node, cols = queue.popleft()
            if node is not None:
                column_table[cols].append(node.val)
                queue.append((node.left, cols - 1))
                queue.append((node.right, cols + 1))

                min_cols = min(min_cols, cols)
                max_cols = max(max_cols, cols)
        return [column_table[i] for i in range(min_cols, max_cols +1)]