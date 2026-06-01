class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        count = 0

        for ops in operations:
            if ops == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
                count += val
                continue
            if ops == "C":
                count -= stack.pop()
                continue
            if ops == "D":
                count += stack[-1]*2
                stack.append(stack[-1]*2)
                continue
            count += int(ops)
            stack.append(int(ops))
        
        return count
        
