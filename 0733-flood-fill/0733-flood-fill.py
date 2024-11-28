class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m=len(image)
        n=len(image[0])
        initialvalue = image[sr][sc]
    
        def recursion(x,y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != initialvalue or image[x][y]==color:
                return
            
            # Update the pixel color
            image[x][y] = color
            
            # Recursive calls for the four neighbors
            recursion(x + 1, y)  # Down
            recursion(x - 1, y)  # Up
            recursion(x, y + 1)  # Right
            recursion(x, y - 1)  # Left
        recursion(sr,sc)
        
        return image
                