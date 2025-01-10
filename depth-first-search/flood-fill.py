class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        #retrieve the current color
        curr_color = image[sr][sc]

        #checks to see if it is the same, if it is, then return original image
        if curr_color == color:
            return image

        #start dfs
        def dfs(image, sr, sc):
            #change old color location to new color 
            image[sr][sc] = color

            list = [[sr-1, sc], [sr+1, sc], [sr, sc+1], [sr, sc-1]]

            for row, col in list:
                if 0 <= row and 0 <= col and row < len(image) and col < len(image[0]) and image[row][col] == curr_color:
                    dfs(image, row, col)

        #calling dfs on the original image, and starting point 
        dfs(image, sr, sc)

        #returning original image
        return image
