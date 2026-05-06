class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        pair = 0
        for num in count:
            if count[num] % 2 == 0:
                pair += count[num] / 2

        return len(nums) / 2 == pair