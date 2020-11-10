from typing import Tuple 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        str_ptr = 0
        token_ptr = 0
        tokens = self.parsePattern(p)
        return self.match(tokens, s, str_ptr, token_ptr)
        
    def match(self, tokens: Tuple[Tuple[str, bool]], string: str, str_ptr: int, token_ptr: int) -> bool:
        # If both the string and pattern are fully consumed, it's a match
        if str_ptr == len(string) and token_ptr == len(tokens):
            return True
        # If the pattern is consumed but the string is not, it's not a match
        if token_ptr == len(tokens):
            return False
        
        char, is_starred = tokens[token_ptr]
        
        # If the string is consumed but the pattern is not
        if str_ptr == len(string):
            # If it's an optional character, then continue
            if is_starred:
                return self.match(tokens, string, str_ptr, token_ptr + 1)
            # Otherwise, it's not a match
            return False
        
        # If neither are consumed:
        
        if is_starred:
            # Since the character is optional, regardless of whether the character matches, try advancing the token pointer
            if self.match(tokens, string, str_ptr, token_ptr + 1):
                return True
            # If the character does match, try advancing the string pointer
            if (char == string[str_ptr] or char == '.') and self.match(tokens, string, str_ptr + 1, token_ptr):
                return True
            # If neither pan out, it's not a match
            return False

        # If the character matches and it's not optional, try advancing both pointers
        return (char == string[str_ptr] or char == '.') and self.match(tokens, string, str_ptr + 1, token_ptr + 1)

            
            
    def parsePattern(self, pattern: str) -> Tuple[Tuple[str, bool]]:
        """Parse a pattern into a tuple of tuples like (char: str, is_starred: bool)"""
        tokens = []
        ptr = 0
        while ptr < len(pattern):
            if ptr + 1 < len(pattern) and pattern[ptr + 1] == '*':
                tokens.append((pattern[ptr], True))
                ptr += 2
            else:
                tokens.append((pattern[ptr], False))
                ptr += 1
        return tokens