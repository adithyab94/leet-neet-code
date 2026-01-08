class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #if the lengths are different, return False
            return False

        for char in set(s):
            if s.count(char)!= t.count(char):
                return False
        return True