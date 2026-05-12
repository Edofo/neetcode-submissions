class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for x in range(i, len(nums)):
                if nums[x]< nums[i]:
                    prev = nums[i]
                    nums[i] = nums[x]
                    nums[x] = prev

        return nums
        