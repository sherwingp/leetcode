class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        
        for i in s:
            if res and res[-1].isupper() and res[-1].lower() == i:
                res.pop(-1)
            elif res and res[-1].islower() and res[-1].upper() == i:
                res.pop(-1)
            else:
                res.append(i)
        return "".join(res)