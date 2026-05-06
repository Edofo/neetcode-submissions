class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        pair = 0
        for num in count.values():
            if num > 1:
                pair += num * (num - 1) // 2

        return pair