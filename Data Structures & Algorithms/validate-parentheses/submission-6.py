class Solution:
    def isValid(self, s: str) -> bool:

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