class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        window_start = len(s) - 1
        window_end = None
        while window_start >= 0:
            if s[window_start].isalpha():
                if not window_end:
                    window_end = window_start
                
                if window_start == 0:
                    return window_end - window_start + 1
            else:
                if window_end:
                    return window_end - window_start
            
            window_start -= 1
