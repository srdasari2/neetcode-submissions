class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        j = len(s) - 1
        i = 0
        s = s.lower()
        print(s)
        print(s[i])
        if len(s) == 1:
            return True
        while i <= j and i < len(s):            
            while not (s[i].isalpha() or s[i].isdigit()) and i < j:
                i += 1
            while not (s[j].isalpha() or s[j].isdigit()) and j > i:
                j -= 1
            if not s[i] == s[j]:
                return False
            i += 1
            j -= 1
        return True