class Solution:
    def numSquares(self, n: int) -> int:
        squares = set()
        queue = []
        count = 0
        for i in range(0,n+1):
            if int(math.sqrt(i)) * int(math.sqrt(i)) == i:
                squares.add(i)
        squares.pop()
        if n in squares:
            return 1
        for ele in squares:
            if n-ele in squares:
                return count+2
            queue.append(n-ele)
        count = count + 1

        while(len(queue) > 0):
            print(queue)
            for i in range(0, len(queue)):
                ele1 = queue.pop(0)
                for num in squares:
                    if ele1-num > 0:
                        if ele1-num in squares:
                            count = count + 1
                            return count + 1
                        queue.append(ele1-num)
            count = count + 1
        return 0