class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = [len(seats)] * len(seats)
        right = [len(seats)] * len(seats)
        output = [len(seats)] * len(seats)
        
        for i in range(0, len(seats)):
            if seats[i] == 1:
                left[i] = 0
            else:
                if i > 0:
                    left[i] = left[i-1] + 1
        
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            else:
                if i < len(seats) -1:
                    right[i] = right[i+1] + 1
        
        for i in range(0, len(seats)):
            output[i] = min(left[i], right[i])
        
        return max(output)