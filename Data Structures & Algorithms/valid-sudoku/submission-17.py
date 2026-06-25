class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            row = board[i]
            row_nums = [num for num in row if num != '.']
            a = len(row_nums)
            b = len(list(set(row_nums)))
            if a != b:
                return False
        
        for i in range(len(board[0])):
            col = [row[i] for row in board]
            col_nums = [num for num in col if num != '.']
            a = len(col_nums)
            b = len(list(set(col_nums)))
            if a != b:
                return False

        for row_incr in range(0, 9, 3):
            for col_incr in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[i + row_incr][j + col_incr])
                box_nums = [num for num in box if num != '.']
                if len(box_nums) != len(set(box_nums)):
                    return False
        
        return True
        