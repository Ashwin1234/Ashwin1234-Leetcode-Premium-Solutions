class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        stack.append(["-1",-1])
        for ele in s:
            if stack[-1][1] == k:
                for i in range(0,k):
                    stack.pop()
            if stack[-1][0] == ele:
                prevCount = stack[-1][1]
                stack.append([ele, prevCount + 1])
            else:
                stack.append([ele, 1])
        stack.pop(0)
        output = ''
        if stack[-1][1] == k:
            for i in range(0,k):
                stack.pop()
        for ele in stack:
            output = output + ele[0]
        return output