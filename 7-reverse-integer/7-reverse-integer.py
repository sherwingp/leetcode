class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            a = abs(x)
        else:
            a = x
    
        b = 0
        
        while a > 0:
            b = b * 10 + a % 10
            a = a//10
        
        if x < 0:
            b = -abs(b)
        else:
            pass
        
        if b < -(2**31) or b > 2**31 - 1:
            return 0
        else:
            return b
    
        