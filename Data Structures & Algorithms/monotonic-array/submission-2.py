class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = None
        for i in range(1, len(nums)):
            if increase is None and nums[i] != nums[i-1]:
                increase = nums[i] > nums[i-1]
            if increase and nums[i] < nums[i-1]:
                return False
            if increase is False and nums[i] > nums[i-1]:
                return False

        return True