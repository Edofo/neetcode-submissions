class Solution:
    def minOperations(self, logs: List[str]) -> int:
        curr = 0

        for log in logs:
            if log == "../":
                curr = max(0, curr - 1)
                continue
            if log == "./":
                continue
            curr += 1
        
        return curr