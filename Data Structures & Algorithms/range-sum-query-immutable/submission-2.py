class NumArray:

    def __init__(self, nums: List[int]):
        self.mapping = defaultdict(list)
        count = 0
        for i, val in enumerate(nums):
            count += val
            self.mapping[i] = count

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.mapping[right]
        return self.mapping[right] - self.mapping[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)