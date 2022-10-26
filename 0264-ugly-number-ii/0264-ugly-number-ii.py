class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heapify(heap)
        factors = [2,3,5]
        output = []
        heappush(heap,1)
        for i in range(1, 1691):
            if len(output) == n:
                break
            j = heappop(heap)
            output.append(j)
            for ele in factors:
                if j*ele not in heap:
                    heappush(heap, j*ele)
                    
        return output[-1]
        
        
                    