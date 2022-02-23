class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights
        expected = sorted(expected)
        count = 0
        for i in range(len(heights)):
            if expected[i]!= heights[i]:
                count = count + 1
        return count