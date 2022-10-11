class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append((temperatures[0], 0))
        output = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i] > stack[-1][0]:
                while(len(stack) > 0 and temperatures[i] > stack[-1][0]):
                    ele = stack.pop(-1)
                    output[ele[1]] = i - ele[1]
                stack.append((temperatures[i],i))
            else:
                stack.append((temperatures[i], i))
        return output
        