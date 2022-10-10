class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        first = [0] * (k+1)
        last = [0] * (k+1)
        max_score = -1
        for i in range(0, k):
            first[i+1] = first[i] + cardPoints[i]
            last[i+1] = last[i] + cardPoints[len(cardPoints) - i - 1]
        print(first)
        print(last)
        for i in range(0, k + 1):
            score = first[i] + last[k - i]
            max_score = max(max_score, score)
        return max_score
            
            