class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
            else:
                current = 0
            count = max(count, current)
                
        
        return count
        