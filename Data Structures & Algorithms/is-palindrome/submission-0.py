class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and self.checkAlphanumeric(s[i]) is False:
                i += 1
            while j > i and self.checkAlphanumeric(s[j]) is False:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    
    def checkAlphanumeric(self, char: str) -> bool:
        if (ord(char) >= ord ('A') and ord(char) <= ord('Z')) or (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('0') and ord(char) <= ord('9')):
            return True
        else:
            return False