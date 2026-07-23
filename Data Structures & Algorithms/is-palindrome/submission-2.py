class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        print(s)
        i = 0
        j = len(s)
        while (i < j):
            if s[i] != s[j-1]:
                return False
            i += 1
            j -= 1
        return True