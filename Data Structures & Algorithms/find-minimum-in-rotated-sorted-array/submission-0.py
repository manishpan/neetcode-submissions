class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n - 1

        while start <= end:
            mid = (start + end) >> 1
            prev = (mid - 1 + n) % n

            if nums[prev] >= nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        