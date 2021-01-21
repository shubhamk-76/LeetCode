from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.paren_generator(n, n))
        
    def paren_generator(self, num_to_open: int, num_to_close: int, string: str = ''):
        if num_to_close == 0:
            yield string
            return
        if num_to_open > 0:
            yield from self.paren_generator(num_to_open - 1, num_to_close, string + '(')
        if num_to_close > num_to_open:
            yield from self.paren_generator(num_to_open, num_to_close - 1, string + ')')