class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bm = collections.defaultdict(list)
        for x in range(9):
            for y in range(9):
                c = board[x][y]
                if c != '.': 
                    if c in bm:
                        for pos in bm[c]:
                            if (pos[0]== x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
                                return False
                    bm[c].append((x,y))
        return True