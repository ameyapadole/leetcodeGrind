class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # r1 - c1 == r2 - c2 
        # Value of Diagonals as Groups[r-c]

  
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))