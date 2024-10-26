class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        temp1=0
        temp2=0
        counter=0
        for i in a[::-1]:
            if i=='1':
                temp1+=2**counter
            counter+=1
        counter=0
        for i in b[::-1]:
            if i=='1':
                temp2 = temp2+2**counter
            counter+=1
        temp3 = bin(temp1+temp2)
        return temp3[2:]
        