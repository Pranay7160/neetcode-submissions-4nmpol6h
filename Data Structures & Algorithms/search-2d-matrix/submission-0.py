class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col_len = len(matrix[0])
        
        for ri in range(row):
            for ci in range(col_len):
                if matrix[ri][ci] == target:
                    return True
        
        return False