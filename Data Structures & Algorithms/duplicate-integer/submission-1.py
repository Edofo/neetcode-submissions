class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab: List[int] = []
        contain = False;
        index = 0

        while index < len(nums) and contain is False:
            num = nums[index]
            if num in tab:
                contain = True
            tab.append(num)
            index = index + 1
        
        return contain
        