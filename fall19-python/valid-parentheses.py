class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False
        
        stack = []
        
        for bracket in s:
            if bracket in '[{(':
                stack.append(bracket)
            elif bracket in ']})' and stack != []:
                if (stack[-1] in '{}' and bracket in '{}') or (stack[-1] in '()' and bracket in '()') or (stack[-1] in '[]' and bracket in '[]'):
                    stack.pop()
                else:
                    return False
        
        if stack != []:
            return False
        return True
            
            
            
        
        
