class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
            
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n = n - 1
        for i in range(1, len(flowerbed) - 1):
            if n == 0:
                return True
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n = n-1
        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            n = n - 1
        print(flowerbed)
        
        if n == 0:
            return True
        else:
            return False