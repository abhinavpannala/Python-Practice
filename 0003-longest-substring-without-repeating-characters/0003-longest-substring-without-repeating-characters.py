class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        dictionary = {}
        maxi = 0
        
        for r in range(len(s)):
            if s[r] in dictionary and dictionary[s[r]] >= l:
                l = dictionary[s[r]] + 1
            dictionary[s[r]] = r
            maxi = max(maxi, r - l + 1)
        
        return maxi


