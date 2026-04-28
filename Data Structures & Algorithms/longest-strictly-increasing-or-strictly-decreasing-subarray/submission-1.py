class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase_count = 0
        decrease_count = 0

        curr_increase = 1
        curr_decrease = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_increase += 1
            else:
                increase_count = max(increase_count, curr_increase)
                curr_increase = 1
            if nums[i] < nums[i - 1]:
                curr_decrease += 1
            else:
                decrease_count = max(decrease_count, curr_decrease)
                curr_decrease = 1

        increase_count = max(increase_count, curr_increase)
        decrease_count = max(decrease_count, curr_decrease)

        return max(increase_count, decrease_count)