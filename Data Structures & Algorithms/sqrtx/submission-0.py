class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x

        while start <= end:
            sqrt = start + (end - start) // 2

            num = sqrt * sqrt

            if num > x:
                end = sqrt - 1
            elif num < x:
                start = sqrt + 1
            else:
                return sqrt
        
        return end