class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""

        for i in range(1, len(num)-1):
            if num[i-1] == num[i] == num[i+1]:
                actual = num[i-1] + num[i] + num[i+1]
                if largest < actual:
                    largest = actual
        
        return str(largest)
                
                
        