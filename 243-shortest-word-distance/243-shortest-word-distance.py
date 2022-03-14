class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        left = -1
        right = -1
        dist = float('inf')
        for i in range(0,len(wordsDict)):
            if wordsDict[i] == word1:
                left = i
            if wordsDict[i] == word2:
                right = i
            if left > -1 and right > -1:
                dist = min(dist, abs(left - right))
        return dist
                
            
                
        