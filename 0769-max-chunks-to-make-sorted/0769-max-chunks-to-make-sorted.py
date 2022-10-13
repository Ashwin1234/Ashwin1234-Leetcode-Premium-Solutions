class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        max1 = float('-inf')
        for i in range(0, len(arr)):
            max1 = max(max1, arr[i])
            if max1 == i:
                count = count + 1
        return count