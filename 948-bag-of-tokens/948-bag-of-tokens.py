class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        result = 0
        left = 0
        right = len(tokens) - 1
        tokens = sorted(tokens)
        while(left <= right):
            print(left, right)
            if tokens[left] <= power:
                power = power - tokens[left]
                score = score + 1
                result = max(result, score)
                left = left + 1
            elif score > 0:
                power = power + tokens[right]
                score = score - 1
                right = right - 1
            else:
                return result
        return result
                
        