class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        window_start = 0
        hash = {}
        
        for window_end, letter in enumerate(s):
            if letter in hash:
                while letter in hash:
                    del hash[s[window_start]]
                    window_start += 1
            hash[letter] = 1
            max_sub = max(max_sub, window_end - window_start + 1)
    
        return max_sub