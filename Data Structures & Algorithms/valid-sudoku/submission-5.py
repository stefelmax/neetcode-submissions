class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                
                number = board[i][j]
                if number != '.':
                    if number in rows[i] or number in columns[j] or number in squares[(i // 3, j // 3)]:
                        return False
                    else:
                        rows[i].add(number)
                        columns[j].add(number)
                        squares[(i // 3, j // 3)].add(number)

        return True
