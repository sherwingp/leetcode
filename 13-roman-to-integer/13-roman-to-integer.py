class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        result = 0
        
        for i in range(0, len(s) - 1):
            if numerals[s[i+1]] > numerals[s[i]]:
                result -= numerals[s[i]]
            else:
                result += numerals[s[i]]
        return result + numerals[s[-1]]
            