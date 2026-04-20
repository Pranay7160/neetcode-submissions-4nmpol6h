class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for b in range(9):
            for i in range(9):
                val = board[b][i]
                if val == '.':
                    continue
                
                r0 = (b//3) * 3
                c0 = (i//3)

                boxi = r0 + c0
                
                if val in row[b] or val in col[i] or val in box[boxi]:
                    return False
                
                row[b].add(val)
                col[i].add(val)

                box[boxi].add(val)
        
        return True
                

        