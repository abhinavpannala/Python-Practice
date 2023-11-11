class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = defaultdict(int)
        for i in s:
            dict1[i]+=1
        for i in range(len(s)):
            if dict1[s[i]]==1:
                return i
        return -1
            
            