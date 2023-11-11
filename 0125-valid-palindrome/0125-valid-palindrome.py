import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]','',s)
        s=cleaned_string.lower()
        if s[:].lower()==s[::-1].lower():

            return True
        else:
            return False