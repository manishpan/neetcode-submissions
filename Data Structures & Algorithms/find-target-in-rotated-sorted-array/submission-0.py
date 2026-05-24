class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) >> 1

            if target == nums[mid]:
                return mid
                
            if target > nums[end]:
                if target > nums[mid] and nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target > nums[mid] or nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1