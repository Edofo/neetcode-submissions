class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tab = []

        for i in range(len(nums1)):
            start = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    start = True
                if nums1[i] < nums2[j] and start:
                    tab.append(nums2[j])
                    break;
                if len(nums2) - 1 == j:
                    tab.append(-1)
        
        return tab
        