class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        nlen=len(needle)
        while i<=len(haystack)-nlen:
            if haystack[i:i+nlen]==needle:
                return i
            i+=1
        return -1
                