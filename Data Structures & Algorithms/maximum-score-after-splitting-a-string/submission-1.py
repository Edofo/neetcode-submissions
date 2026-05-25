class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count("1")
        zeros_left = 0
        ones_left = 0
        max_value = 0
        
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros_left += 1
            else:
                ones_left += 1
            score = zeros_left + (total_ones - ones_left)
            max_value = max(max_value, score)
        
        return max_value