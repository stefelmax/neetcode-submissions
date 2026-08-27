class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                t = (i // 3, j // 3)

                if element != '.' and (element in rows[i] or element in columns[j] or element in square[t]):
                    return False
                else:
                    rows[i].add(element)
                    columns[j].add(element)
                    square[t].add(element)

        return True

                


        