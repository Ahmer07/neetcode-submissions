class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        alpha_numeric = "qwertyuioplkjhgfdsazxcvbnm1234567890"
        s = s.lower()
        s = s.replace(" ", "")
        for i in s[::-1]:
            if i not in alpha_numeric:
                s = s.replace(i, "")
                continue
            new_str += i.lower()
        print(new_str)
        print(s)
        if new_str == s:
            return True
        return False

        