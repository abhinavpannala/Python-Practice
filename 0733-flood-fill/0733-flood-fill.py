class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m=0
        n=0
        for i in image:
            m+=1
            n=0
            for j in i:
                n+=1
        initialvalue = image[sr][sc]
        if initialvalue == color:
            return image
        def recursion(x,y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != initialvalue:
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
                