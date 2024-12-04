class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a),len(b))
        carry=0
        res=""
        a,b = a[::-1],b[::-1]
        for i in range(max_len):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i<len(b) else 0
            intermediate = digitA+digitB+carry
            char = str(intermediate%2)
            res = char + res
            carry = intermediate//2
        if carry == 1:
            res = "1"+res
        return res