class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        colorized = [[0] * len(image[0]) for _ in range(len(image))]
        
        self.colorize(image, colorized, sr, sc, image[sr][sc], color)

        return image
    
    def colorize(self, image, colorized, sr, sc, oldColor, newColor):

        if sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0]):
            if image[sr][sc] == oldColor and colorized[sr][sc] == 0:

                image[sr][sc] = newColor
                colorized[sr][sc] = 1

                self.colorize(image, colorized, sr-1, sc, oldColor, newColor)
                self.colorize(image, colorized, sr, sc+1, oldColor, newColor)
                self.colorize(image, colorized, sr+1, sc, oldColor, newColor)
                self.colorize(image, colorized, sr, sc-1, oldColor, newColor)


