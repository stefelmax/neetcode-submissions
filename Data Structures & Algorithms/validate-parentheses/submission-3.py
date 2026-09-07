class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False
        
        mapping = {']': '[', '}': '{', ')': '('}
        stack = []

        for symbol in s:
            if symbol in mapping:
                if not stack or mapping[symbol] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(symbol)

        return True if not stack else False

