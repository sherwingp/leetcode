class Solution:
    def isValid(self, s: str) -> bool:
        dict = { '(': ')', '[': ']', '{': '}'}
        stack = []
        
        if len(s) < 2:
            return False
        
        for i in range(len(s)):
            # If an opening bracket add to stack
            if s[i] in dict:
                stack.append(s[i])
            # If a closing bracket doesn't complement last in stack
            elif len(stack) == 0:
                return False
            elif s[i] != dict[stack.pop(-1)]:
                return False
        # Return true if stack is empty
        if len(stack) == 0:
            return True