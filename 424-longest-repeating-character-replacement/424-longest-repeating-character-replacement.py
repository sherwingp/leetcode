class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        mode = 0
        res = 0
        
        l = 0
        
        for r, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            mode = max(freq.values())
            
            while r - l + 1 - mode > k:
                freq[s[l]] = freq[s[l]] - 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
                
            