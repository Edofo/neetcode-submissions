class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        pair = 0
        for num in count.values():
            if num > 1:
                for i in range(0, num - 1):
                    pair += i + 1


        return pair