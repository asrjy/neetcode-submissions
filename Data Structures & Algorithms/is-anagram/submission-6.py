class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ords_a = [0 for i in range(26)]
        ords_b = [0 for i in range(26)]
        if len(s) != len(t):
            return False
        for char in s.lower():
            ords_a[ord(char) - 97] += 1
        for char in t.lower():
            ords_b[ord(char) - 97] += 1
        if ords_a == ords_b:
            return True
        return False