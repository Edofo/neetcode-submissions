class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        curr = nums[0]

        for x in count:
            if count[curr] < count[x]:
                curr = x

        return curr