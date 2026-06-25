class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}": "{",
            "]": "[",
            ")" : "("
        }
        stack = []
        for b in s:
            if b in brackets.values():
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False

