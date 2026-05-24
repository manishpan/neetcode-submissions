class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        res = 1

        while start <= end:
            capacity = (start + end) >> 1
            days_taken = 1
            currCap = capacity

            for w in weights:
                if currCap - w < 0:
                    days_taken += 1
                    currCap = capacity
                currCap -= w
            
            if days_taken > days:
                start = capacity + 1
            else:
                res = capacity
                end = capacity - 1
        
        return res
            
