class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = 0
        for b in range(len(nums)):
            prev = nums[b]
            nums[b] = 2
            if prev < 2:
                nums[w] = 1
                w += 1
            if prev < 1:
                nums[r] = 0
                r += 1
                