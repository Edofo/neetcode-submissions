class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        tab = set()
        idx = 0

        for num in nums2:
            if num in set1:
                tab.add(num)

        return list(tab)