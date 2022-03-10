class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.squared(n)
        fast = self.squared(self.squared(n))
        
        while slow is not fast and fast is not 1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))
        return fast == 1
    
        
    def squared(self, slow):
        res = 0
        while slow:
            digit = slow % 10
            digit = digit ** 2
            res += digit
            slow = slow // 10
        return res