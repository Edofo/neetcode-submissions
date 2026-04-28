class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxVal = nums[0]
        currMax = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currMax += nums[i]
                continue
            maxVal = max(maxVal, currMax)
            currMax = nums[i]

        return max(maxVal, currMax)
        