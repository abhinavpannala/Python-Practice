import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s1=""
        sign=1
        s=s.strip()
        index = 0
        if len(s)==0: return 0
        if s[0]=="+":
            index+=1
        elif s[0]=="-":
            sign=-1
            index+=1
        while(index<len(s) and s[index].isdigit()):
            s1 = s1+ s[index] 
            index+=1
        result = int(s1) if s1 else 0 
        return max( -2**31, min( sign*result, 2**31 - 1 ) )

