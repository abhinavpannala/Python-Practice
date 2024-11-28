class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictionary = {}
        for i in s:
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1
        for i in t:
            if i in dictionary:
                dictionary[i]-=1
            else:
                return False
        for k in dictionary.values():
            if k!=0:
                return False
        return True