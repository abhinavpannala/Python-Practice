class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j=len(a)-1, len(b)-1
        carry = 0
        res=""
        while i>=0 or j>=0:
            temp = carry
            if i>=0:
                temp+=int(a[i])
                i-=1
            if j>=0:
                temp+=int(b[j])
                j-=1
            res = str(temp%2)+res
            carry = temp // 2
        if carry:
            res = "1"+res
        return res