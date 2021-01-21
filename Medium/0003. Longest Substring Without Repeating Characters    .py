class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for idx in range(len(s)):
            substr_len = self.getSubstringLength(s[idx:])
            if substr_len > longest:
                longest = substr_len
        return longest
        
        
    def getSubstringLength(self, s: str) -> str:
        chars = set()
        for idx, char in enumerate(s):
            if char in chars:
                return len(chars)
            chars.add(char)
        return len(chars)