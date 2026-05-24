class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = 1

        while start <= end:
            k = (start + end) >> 1
            time_taken = 0

            for i in piles:
                time_taken += math.ceil(i/k)

            if time_taken > h:
                start = k + 1
            else:
                res = k
                end = k - 1

        return res    