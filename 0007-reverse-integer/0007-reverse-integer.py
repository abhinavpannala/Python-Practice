class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
           result = int(str(x)[::-1])
        else:
            result = -1*int(str(x)[1:][::-1])
        return result if result.bit_length() < 32 else 0