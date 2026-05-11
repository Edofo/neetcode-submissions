class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for x in range(i, len(nums)):
                if nums[i] > nums[x]:
                    prev = nums[i]
                    nums[i] = nums[x]
                    nums[x] = prev

        return nums
        