class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_s = [set() for _ in range(9)]
        col_s = [set() for _ in range(9)]
        box = defaultdict(set) # tuple will be key

        # this 2 loops will go to each element in matrix
        for r in range(9): # 9 row
            for c in range(9):
                val = board[r][c] # acceing each value by row and col
                if val == ".":
                    continue

                box_i = (r//3, c//3) # it wil become key for box dict
                if val in row_s[r] or val in col_s[c] or val in box[box_i]:
                    return False
                
                row_s[r].add(val)
                col_s[c].add(val)
                box[box_i].add(val)
            
        
        return True