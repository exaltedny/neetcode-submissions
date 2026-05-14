class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for chr in s:
                if chr not in t:
                    return False 
                else:
                    t = t.replace(chr,"", 1)
            return True

