class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word_dict = {}
        for i in magazine:
            if i not in word_dict:
                word_dict[i]=1
            else:
                word_dict[i]+=1
        for i in ransomNote:
            if i in word_dict:
                word_dict[i]-=1
                if word_dict[i]==0:
                    word_dict.pop(i)
            else:
                return False
        return True