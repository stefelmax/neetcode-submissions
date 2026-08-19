class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        flag = True
        rows = dict()
        columns = dict()
        squares = dict()


        for n in range(3, 10, 3):
            for m in range(3, 10, 3):
                key = str(n) + str(m)
                i = n - 3
                
                while i < n:
                    j = m - 3
                    while j < m:
                        element = board[i][j]
                        if element != '.':
                            squares.setdefault(key, set())
                            rows.setdefault(i, set())
                            columns.setdefault(j, set())
                            if element in squares[key] or element in rows[i] or element in columns[j]:
                                return False
        
                            else:
                                squares[key].add(element)
                                rows[i].add(element)
                                columns[j].add(element)
                        j += 1
                    i += 1
        return True


        