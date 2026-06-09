class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)
        for num in nums:
            if num >= len(nums):
                count[len(nums)] += 1
            else:
                count[num] += 1
        
        total = 0
        for x in range(len(nums), 0, -1):
            total += count[x]
            if total == x:
                return x
        return -1