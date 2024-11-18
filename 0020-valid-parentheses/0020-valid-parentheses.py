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
        last_opened = []
        for item in s:
            if last_opened and item == hash.get(last_opened[-1]):
                stack.pop()
                last_opened.pop()
            else:
                last_opened.append(item)
                stack.append(item)
        if stack:
            return False
        else:
            return True
        