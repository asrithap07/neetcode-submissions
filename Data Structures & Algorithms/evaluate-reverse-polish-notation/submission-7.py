class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        stack = []

        #loop through tokens
        for token in tokens:
            #if its a operator
            if token in operators:
                #pop off the left and the right value
                right = stack.pop()
                left = stack.pop()
                #push the result of the operand onto the stack
                stack.append(int(operators[token](left, right)))
            #if its a value add to the stack
            else:
                stack.append(int(token))
        
        return stack[0]
