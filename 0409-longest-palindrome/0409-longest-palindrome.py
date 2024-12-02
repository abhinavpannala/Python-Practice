class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1 = {}
        counter = 0
        odd_found = False
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in dict1.keys():
            if dict1[i]%2==0:
                counter+=dict1[i]
            else:
                counter+=dict1[i]-1
                odd_found = True
        if odd_found:
            counter+=1
        return counter
