class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False