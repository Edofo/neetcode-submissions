class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        return sorted(nums, key=lambda x: (count[x], -x))