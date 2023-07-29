class Solution:
    def isValid(self, s: str) -> bool:
        stack = [""]
        pairs = dict(zip((')', ']', '}'),('(','[', '{')))
        for c in s:
            if c in pairs:
                if pairs[c] == stack[-1]:
                    stack.pop()
                    continue
                return False # miss match closing parenthese
            stack.append(c)
        return len(stack) == 1


