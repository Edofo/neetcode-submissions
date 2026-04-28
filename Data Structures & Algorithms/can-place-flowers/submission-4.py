class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = 0
            right = 0
            if i > 0:
                left = flowerbed[i-1]
            if i < len(flowerbed) - 1:
                right = flowerbed[i+1]
            if left == 0 and flowerbed[i] == 0 and right == 0:
                n -= 1
                flowerbed[i] = 1

            if n <= 0:
                return True


        return False
        