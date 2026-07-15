class Solution:
    def isValid(self, s: str) -> bool:

        #make hashmap with valid pairs
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        #declare stack
        stack = []

        #loop through string
        for b in s:
            #if its an open
            if b in brackets.values():
                #add to the stack
                stack.append(b)
            #else if closed
            elif b in brackets:
                #if theres no opening brackets yet -> ret false
                if not stack:
                    return False

                #if the current closing with most recent opening dont correspond -> ret false
                if stack and not (stack.pop() == brackets[b]):
                    return False
        
        return len(stack) == 0
    
