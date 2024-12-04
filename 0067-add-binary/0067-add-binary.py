class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j=len(a)-1, len(b)-1
        carry = 0
        ans=[]
        while i>=0 or j>=0 or carry:
            temp = carry
            if i>=0:
                temp+=int(a[i])
                i-=1
            if j>=0:
                temp+=int(b[j])
                j-=1
            ans += str(temp % 2) 
            carry = temp // 2
        return "".join(ans[::-1])