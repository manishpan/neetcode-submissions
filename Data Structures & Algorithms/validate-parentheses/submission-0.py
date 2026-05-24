class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = { ')': '(', '}':'{', ']': '[' }
        stack = [-1]

        for i in s:
            if i in {'(', '{', '['}:
                stack.append(i)
            else:
                a = stack.pop()
                if a != p_dict.get(i):
                    return False
        
        if stack[-1] == -1:
            return True
        
        return False