class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = -1
        index2 = -1
        minDist = float('inf')
        for i in range(0,len(wordsDict)):
            if wordsDict[i] == word1:
                index1 = i
            if wordsDict[i] == word2:
                index2 = i
            if abs(index1 - index2) < minDist and (index1>=0 and index2>=0):
                minDist = abs(index1 - index2)
        return minDist
        