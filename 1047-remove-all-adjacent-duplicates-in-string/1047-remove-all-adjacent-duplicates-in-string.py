class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        stack.append("-1")
        for i in range(0, len(s)):
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        stack.pop(0)
        return ''.join(stack)
        