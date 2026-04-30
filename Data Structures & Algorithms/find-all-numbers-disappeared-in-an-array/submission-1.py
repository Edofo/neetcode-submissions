class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = set()

        for i in range(1, len(nums) + 1):
            missing.add(i)
        
        for num in nums:
            if num in missing:
                missing.remove(num)
        
        return list(missing)