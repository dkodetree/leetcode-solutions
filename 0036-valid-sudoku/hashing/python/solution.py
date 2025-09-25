class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Track seen values in rows, columns, and 3x3 sub-sudoku boxes
        row_map = collections.defaultdict(set)  # row index -> values set
        col_map = collections.defaultdict(set)  # col index -> values set
        sub_sudoku_map = collections.defaultdict(set) # (row // 3, col // 3) -> values set

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                if (value in row_map[row] or 
                      value in col_map[col] or
                      value in sub_sudoku_map[(row // 3, col // 3)]):
                      return False
                row_map[row].add(value)
                col_map[col].add(value)
                sub_sudoku_map[(row // 3, col // 3)].add(value)
        return True
