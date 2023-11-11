class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
        s=cleaned_string.lower()
        if s[:].lower()==s[::-1].lower():

            return True
        else:
            return False