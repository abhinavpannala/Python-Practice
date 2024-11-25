class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_string = cleaned_string.lower()
        if cleaned_string == cleaned_string[::-1]:
            return True
        else:
            return False