class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for idx in range(len(s)):
            substr = self.getSubstring(s[idx:])
            if len(substr) > len(longest):
                longest = substr
        return longest
        
        
    def getSubstring(self, s: str) -> str:
        for end_idx in range(len(s), 1, -1):
            if s[:end_idx] == s[end_idx-1::-1]:
                return s[:end_idx]
        return s[0]