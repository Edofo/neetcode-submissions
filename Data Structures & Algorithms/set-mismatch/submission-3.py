class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        find_nums = set()
        for i in range(1, len(nums) + 1):
            find_nums.add(i)

        duplicate = 0
        for num in nums:
            if num not in find_nums:
                duplicate = num
                continue
            find_nums.remove(num)

        return [duplicate, find_nums.pop()]