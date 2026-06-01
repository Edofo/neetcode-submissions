class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        count = 0

        for ops in operations:
            if ops == "+":
                val = stack[len(stack)-1] + stack[len(stack)-2]
                stack.append(val)
                count += val
                continue
            if ops == "C":
                count -= stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                continue
            if ops == "D":
                count += stack[len(stack)-1]*2
                stack.append(stack[len(stack)-1]*2)
                continue
            count += int(ops)
            stack.append(int(ops))
        
        return count
        
