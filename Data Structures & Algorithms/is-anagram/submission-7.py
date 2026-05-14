class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for chr in s:
                if s.count(chr) != t.count(chr):
                    return False
            return True