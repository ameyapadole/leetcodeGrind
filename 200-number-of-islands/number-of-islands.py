class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid:
            return 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                        res += 1
                        self.dfs(grid, r, c)
        return res 
    
    def dfs(self, grid, r, c):
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0"): #Checking out of bounds
            return
        grid[r][c] = "0" # Mark cell as visited 
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)

