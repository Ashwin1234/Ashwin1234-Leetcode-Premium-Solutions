class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        list1 = list(palindrome)
        isa = 0
        if len(palindrome) == 1:
            return ""
        for i in range(0, int(len(list1)/2)):
            if list1[i]!='a':
                list1[i] = 'a'
                isa = 1
                break
        if isa == 0:
            list1[-1] = 'b'
            return "".join(list1)
        return "".join(list1)