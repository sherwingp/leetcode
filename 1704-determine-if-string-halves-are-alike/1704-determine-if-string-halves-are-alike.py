class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        a_vowels = 0
        b_vowels = 0
        
        vowels = 'aeiouAEIOU'
    
        while l < r:
            if s[l] in vowels:
                a_vowels += 1
            
            if s[r] in vowels:
                b_vowels += 1
        
            l += 1
            r -= 1

        print(a_vowels)
        print(b_vowels)
        
        return a_vowels == b_vowels