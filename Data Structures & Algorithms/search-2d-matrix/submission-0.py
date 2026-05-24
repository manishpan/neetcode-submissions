class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m-1

        while l <= r:
            m = (l + r) >> 1

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                break
        
        start, end = 0, n-1

        while start <= end:
            mid = (start + end) >> 1

            if matrix[m][mid] < target:
                start = mid + 1
            elif matrix[m][mid] > target:
                end = mid - 1
            else:
                return True
        
        return False