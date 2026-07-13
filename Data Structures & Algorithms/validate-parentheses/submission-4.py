class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if stack and brackets[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0