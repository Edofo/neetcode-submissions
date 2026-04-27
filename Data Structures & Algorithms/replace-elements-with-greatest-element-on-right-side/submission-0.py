class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        idx = len(arr) - 2
        maxValue = arr[-1]
        arr[-1] = -1

        while idx > -1:
            tamp = arr[idx]
            arr[idx] = maxValue
            maxValue = max(tamp, maxValue)
            idx -= 1
        
        return arr