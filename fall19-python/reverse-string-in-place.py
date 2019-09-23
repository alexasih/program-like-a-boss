def reverse(list_of_chars):

    # STACK SOLUTION - NOT IN-PLACE
    
    class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # strings are immutable - this is why we are using char
        # so in a real string problem, first convert the string into a list
        
        ret = []
        queue = []
        for val in s:
            queue.append(val)
        
        while queue:
            val = queue.pop()
            ret.append(val)
        
        return ret
    
    # IN-PLACE OPTIMIZED SOLUTION 
    
    # Reverse the input list of chars in place
    temp = ''
    val=0
    rev=-1
    while val < len(list_of_chars)//2:
        
        temp = list_of_chars[val]
        list_of_chars[val] = list_of_chars[rev]
        list_of_chars[rev] = temp
        
        val+=1
        rev-=1
        
    pass

# ANOTHER IN-PLACE SOLUTION (SIMILAR TO ABOVE)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # strings are immutable - this is why we are using char
        # so in a real string problem, first convert the string into a list
        
        val = len(s)-1
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[val]
            s[val] = temp
            val -= 1
            
            
# ONE LINE PYTHON SOLUTION

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # strings are immutable - this is why we are using char
        # so in a real string problem, first convert the string into a list
        
        return s.reverse()
            
            
        
