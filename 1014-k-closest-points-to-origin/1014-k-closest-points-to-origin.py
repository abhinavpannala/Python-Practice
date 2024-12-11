class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict1 = {}
        list1 = []
        for i in range(len(points)):
            ans = points[i][0]**2+points[i][1]**2
            dict1[i]=ans
        dict1 = dict(sorted(dict1.items(), key=lambda item: item[1]))
        for i in range(k):
             list1.append(points[list(dict1.keys())[i]])
        return list1
        

        