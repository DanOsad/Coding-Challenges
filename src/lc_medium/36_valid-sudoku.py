# https://leetcode.com/problems/valid-sudoku/

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [[False] * 9 for _ in range(9)]
        column_check = [[False] * 9 for _ in range(9)]
        sub_box_check = [[False] * 9 for _ in range(9)]

        for row_idx in range(9):
            for col_idx in range(9):
                cell_val = board[row_idx][col_idx]

                if cell_val == '.':
                    continue

                digit_idx = int(cell_val) - 1

                sub_box = (row_idx // 3) * 3 + (col_idx // 3)

                if (row_check[row_idx][digit_idx] or
                    column_check[col_idx][digit_idx] or
                    sub_box_check[sub_box][digit_idx]):
                    return False
                
                row_check[row_idx][digit_idx] = True
                column_check[col_idx][digit_idx] = True
                sub_box_check[sub_box][digit_idx] = True

        return True

cases = [
    {
        'input': [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]],
        'solution': True
    },
    {
        'input': [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]],
        'solution': False
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().isValidSudoku
    }
)
test_suite.run_tests()