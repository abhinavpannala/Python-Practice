class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        empty_list = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                empty_list.append(intervals[i])
                i+=1
            elif (newInterval[0] <= intervals[i][1]) and (intervals[i][0] <= newInterval[1]):
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                i+=1
            else:
                break
        empty_list.append(newInterval)
        while i<len(intervals):
            empty_list.append(intervals[i])
            i+=1
        return empty_list
        




        