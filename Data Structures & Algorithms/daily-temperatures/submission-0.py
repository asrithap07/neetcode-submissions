class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        #loop through the temperatures
        for i in range(len(temperatures)):
            #while the top of the stack is less than the curr value
            while stack and stack[-1][1] < temperatures[i]:
                #pop it off and save the difference of indexes under its index in res
                val = stack.pop()
                res[val[0]] = (i - val[0])
            #push the newest index and value onto the stack as a tuple
            stack.append((i, temperatures[i]))
        
        return res
