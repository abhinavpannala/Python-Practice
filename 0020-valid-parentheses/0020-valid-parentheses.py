class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hash = {}
        hash['(']=')'
        hash['{']='}'
        hash['[']=']'
        for item in s:
            if stack and item == hash.get(stack[-1]):
                stack.pop()
            else:
                stack.append(item)
        if stack:
            return False
        else:
            return True
        