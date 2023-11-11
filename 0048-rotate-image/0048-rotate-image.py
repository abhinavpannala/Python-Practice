class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #reverse
        up = 0
        down = len(matrix)
        for i in range(len(matrix)):
            if up<down:
                matrix[up],matrix[down-1]=matrix[down-1],matrix[up]
                up+=1
                down-=1
        #transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
    
