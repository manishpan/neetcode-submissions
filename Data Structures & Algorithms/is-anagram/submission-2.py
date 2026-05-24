class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        ls = [0] * 26

        if len_s != len_t:
            return False
        
        for i in range(len_s):
            ls[ord(s[i]) - ord('a')] += 1
            ls[ord(t[i]) - ord('a')] -= 1
        
        for i in ls:
            if i != 0:
                return False
        
        return True