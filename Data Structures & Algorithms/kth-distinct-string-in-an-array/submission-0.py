class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for x in arr:
            if x in count:
                count[x] += 1
                continue
            count[x] = 1
        
        print(count)

        number = 0

        for x in count:
            if count[x] == 1:
                number += 1
            if number == k:
                return x
        
        return ""
