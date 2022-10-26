class Solution:
    def isDivisible(self, number, factor):
        while(number%factor == 0):
            number = number/factor
        return number
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [2,3,5]
        for ele in factors:
            n = self.isDivisible(n, ele)
        if n == 1:
            return True
        else:
            return False
        