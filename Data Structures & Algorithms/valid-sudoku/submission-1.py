class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == '.':
                    continue
                
                tpl = (i // 3, j // 3)
                if number in rows[i] or number in columns[j] or number in squares[tpl]:
                    return False

                rows[i].add(number)
                columns[j].add(number)
                squares[tpl].add(number)

        return True
        