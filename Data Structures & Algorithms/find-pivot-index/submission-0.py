class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            total += num

        total_left = 0

        for i in range(len(nums)):
            if total_left == total - total_left - nums[i]:
                return i
            total_left += nums[i]
        
        return -1