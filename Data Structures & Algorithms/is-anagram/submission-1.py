class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        i_letters = {}
        j_letters = {}
        for i in s:
            if i in i_letters:
                i_letters[i] += 1
            else:
                i_letters[i] = 1
        for i in t:
            if i in j_letters:
                j_letters[i] += 1
            else:
                j_letters[i] = 1
        if len(i_letters) != len(j_letters):
            return False
        for k in i_letters:
            if i_letters[k] != j_letters.get(k, 0):
                return False 
        return True
        