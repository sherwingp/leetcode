# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        while l <= r:
            m = l + ((r - l) // 2)
            
            if isBadVersion(m):
                if not isBadVersion(m - 1):
                    return m
                else:
                    r = m - 1
            else:
                l = m + 1