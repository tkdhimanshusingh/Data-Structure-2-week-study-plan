class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        r, c = len(matrix), len(matrix[0])
        l, h = 0, r * c - 1
        while l <= h:
            m = (l + h) // 2
            n = matrix[m // c][m % c]

            if n == target:
                return True
            elif n < target:
                l = m + 1
            else:
                h = m - 1
        
        return False