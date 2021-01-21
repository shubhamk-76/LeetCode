class Solution:
    numbers = set('1234567890')
    
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        int_max = (2 ** 31) - 1
        int_min = -(2 ** 31)
        length = len(s)
        ord_0 = ord('0')
        
        sign = 1
        
        if length == 0:
            return 0
        
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
            length -= 1
        
        if length == 0 or s[0] not in self.numbers:
            return 0
        
        num = 0
        for char in s:
            if char not in self.numbers:
                return max(int_min, min(int_max, num * sign))
            num *= 10
            num += ord(char) - ord_0
        return max(int_min, min(int_max, num * sign))
        
