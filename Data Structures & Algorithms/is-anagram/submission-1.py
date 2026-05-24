class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        ls = [0] * 26

        if len_s != len_t:
            return False
        
        for i in s:
            ls[ord(i) - ord('a')] += 1
        
        for i in t:
            ls[ord(i) - ord('a')] -= 1
        
        for i in ls:
            if i != 0:
                return False
        
        return True