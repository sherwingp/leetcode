class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for window_start in range(0, len(haystack) - len(needle) + 1):
    
            if haystack[window_start] == needle[0]:
                window_end = window_start
                
                while window_end - window_start <= len(needle):
                    if haystack[window_start:window_end] == needle:
                        return window_start
                    window_end += 1
        return -1
                    