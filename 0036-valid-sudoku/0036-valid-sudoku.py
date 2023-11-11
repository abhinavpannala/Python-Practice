class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for i in range(n)]
        columns = [set() for i in range(n)]
        square = [set() for i in range(n)]
        for i in range(n):
            for j in range(n):
                value = board[i][j]
                if value == ".":
                    continue
                if value not in rows[i]:
                    rows[i].add(value)
                else: return False
                if value not in columns[j]:
                    columns[j].add(value)
                else: return False
                sqr = i//3 * 3 + j//3
                if value not in square[sqr]:
                    square[sqr].add(value)
                else: return False
        return True
            