class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_values, min_values = [-float("inf"), -float("inf")], [float("inf"), float("inf")]

        print(max_values, min_values)

        for num in nums:
            print(num, max_values[1])
            if num > max_values[1]:
                if num > max_values[0]:
                    max_values[1] = max_values[0]
                    max_values[0] = num
                else:
                    max_values[1] = num

            if num < min_values[0]:
                if num < min_values[1]:
                    min_values[0] = min_values[1]
                    min_values[1] = num
                else:
                    min_values[0] = num

        print(max_values, min_values)

        return (max_values[0] * max_values[1]) - (min_values[0] * min_values[1])
        