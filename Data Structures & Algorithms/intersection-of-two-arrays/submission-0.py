class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tab = set()
        idx = 0

        while idx < len(nums1) and idx < len(nums2):
            if nums1[idx] in nums2:
                tab.add(nums1[idx])
            if nums2[idx] in nums1:
                tab.add(nums2[idx])
            idx += 1

        return list(tab)