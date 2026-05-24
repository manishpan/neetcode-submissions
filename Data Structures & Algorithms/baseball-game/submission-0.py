class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b)
                stack.append(a)
                stack.append(a + b)
            elif i == 'D':
                a = stack.pop()
                stack.append(a)
                stack.append(2 * a)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        
        return sum(stack)